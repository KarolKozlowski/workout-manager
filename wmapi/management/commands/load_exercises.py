import json
from pathlib import Path

from django.core.management.base import BaseCommand

from wmapi.models import BodyPart, Equipment, Exercise, Muscle


class Command(BaseCommand):
    help = "Load lookup fixtures (bodyparts, equipments, muscles) into DB."

    def add_arguments(self, parser):
        parser.add_argument(
            "--fixtures-dir",
            dest="fixtures_dir",
            help=(
                "Directory containing fixtures (defaults to wmapi/fixtures inside app)."
            ),
        )

    def handle(self, *args, **options):
        fixtures_dir = options.get("fixtures_dir")
        if fixtures_dir:
            base = Path(fixtures_dir)
        else:
            base = Path(__file__).resolve().parents[2] / "fixtures"

        if not base.exists():
            self.stderr.write(f"Fixtures directory not found: {base}")
            return

        mapping = [
            ("bodyparts.json", BodyPart),
            ("equipments.json", Equipment),
            ("muscles.json", Muscle),
        ]

        summary = {}
        for fname, model in mapping:
            path = base / fname
            created = 0
            skipped = 0
            if not path.exists():
                self.stderr.write(f"Missing fixture file: {path}")
                summary[fname] = "missing"
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:  # pragma: no cover - error handling
                self.stderr.write(f"Failed to parse {path}: {exc}")
                summary[fname] = "error"
                continue

            for item in data:
                name = item.get("name")
                if not name:
                    skipped += 1
                    continue
                obj, was_created = model.objects.get_or_create(name=name)
                if was_created:
                    created += 1

            summary[fname] = {
                "created": created,
                "skipped": skipped,
                "total": len(data),
            }

        for k, v in summary.items():
            self.stdout.write(f"{k}: {v}")

        # Also import exercises.json into the Exercise model. This file
        # contains objects with keys like `exerciseId`, `name`, `gifUrl`,
        # and list fields for `targetMuscles`, `bodyParts`, `equipments`,
        # `secondaryMuscles`, `instructions`.
        fname = "exercises.json"
        exercises_path = base / fname

        # Load exercises (potentially large). Use exerciseId as the unique
        # identifier when present; otherwise fall back to name-based create.
        if exercises_path.exists():
            try:
                exercises_data = json.loads(exercises_path.read_text(encoding="utf-8"))
            except Exception as exc:  # pragma: no cover - error handling
                self.stderr.write(f"Failed to parse {exercises_path}: {exc}")
                return

            created = 0
            updated = 0
            skipped = 0

            for item in exercises_data:
                name = item.get("name")
                if not name:
                    skipped += 1
                    continue

                obj, was_created = Exercise.objects.update_or_create(name=name)
                if was_created:
                    created += 1
                else:
                    updated += 1

                obj.name = name
                obj.image_url = item.get("imageUrl") or item.get("image_url")

                obj.video_url = item.get("videoUrl") or item.get("video_url")
                obj.overview = item.get("overview")
                obj.keywords = item.get("keywords") or []
                obj.exercise_tips = item.get("exerciseTips") or item.get(
                    "exercise_tips"
                )
                obj.variations = item.get("variations")
                # obj.related_exercise_ids =
                obj.instructions = item.get("instructions") or []
                obj.exercise_type = item.get("exerciseType") or item.get(
                    "exercise_type"
                )
                obj.target_muscles.set(
                    Muscle.objects.filter(
                        name__in=item.get("targetMuscles")
                        or item.get("target_muscles")
                        or []
                    ).values_list("id", flat=True)
                )
                obj.secondary_muscles.set(
                    Muscle.objects.filter(
                        name__in=item.get("secondaryMuscles")
                        or item.get("secondary_muscles")
                        or []
                    ).values_list("id", flat=True)
                )
                obj.body_parts.set(
                    BodyPart.objects.filter(
                        name__in=item.get("bodyParts") or item.get("body_parts") or []
                    ).values_list("id", flat=True)
                )
                obj.equipments.set(
                    Equipment.objects.filter(
                        name__in=item.get("equipments") or item.get("equipment") or []
                    ).values_list("id", flat=True)
                )
                obj.save()

            exercises_summary = {
                "created": created,
                "skipped": skipped,
                "total": len(exercises_data),
            }
            self.stdout.write(f"{fname}: {exercises_summary}")

        else:
            self.stdout.write("exercises.json: missing")
