import json
from pathlib import Path

from django.core.management.base import BaseCommand

from wmapi.models import Exercise, ExerciseInstance, Set, Workout, WorkoutPart


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

        fname = "workouts.json"
        workouts_path = base / fname

        if workouts_path.exists():
            try:
                workouts_data = json.loads(workouts_path.read_text(encoding="utf-8"))
            except Exception as exc:  # pragma: no cover - error handling
                self.stderr.write(f"Failed to parse {workouts_path}: {exc}")
                return

            created = 0
            updated = 0
            skipped = 0

            for item in workouts_data:
                print(item)
                name = item.get("name")
                id = item.get("id")

                obj, was_created = Workout.objects.update_or_create(id=id)
                if was_created:
                    created += 1
                else:
                    updated += 1

                if not name:
                    skipped += 1
                    continue

                obj.name = name
                obj.description = item.get("description")
                obj.duration_minutes = item.get("duration_minutes")
                obj.start_datetime = item.get("start_datetime")
                obj.end_datetime = item.get("end_datetime")
                obj.notes = item.get("notes")

                for workout_parts in item.get("workout_parts", []):
                    workout_parts_obj, _ = WorkoutPart.objects.update_or_create(
                        id=workout_parts.get("id")
                    )
                    workout_parts_obj.type = workout_parts.get("type")
                    workout_parts_obj.notes = workout_parts.get("notes")
                    print("---")
                    print("WP  ", workout_parts)

                    for exercises in workout_parts.get("exercises", []):
                        defaults = {
                            "exercise_id": Exercise.objects.get(
                                name=exercises.get("exercise_id")
                            ),
                            "notes": exercises.get("notes"),
                        }
                        exercise_obj, _ = ExerciseInstance.objects.update_or_create(
                            id=exercises.get("id"), defaults=defaults
                        )

                        print("EX    ", exercises)
                        print("EX obj   ", exercise_obj)

                        for sets in exercises.get("sets", []):
                            print("SET     ", sets)
                            set_obj, was_created = Set.objects.update_or_create(
                                id=sets.get("id")
                            )
                            set_obj.repetitions = sets.get("repetitions")
                            set_obj.weight = sets.get("weight")
                            set_obj.rest_seconds = sets.get("rest_seconds")
                            set_obj.notes = sets.get("notes")
                            exercise_obj.sets.add(set_obj)
                            set_obj.save()

                        exercise_obj.save()
                        workout_parts_obj.exercises.add(exercise_obj)
                    workout_parts_obj.save()

                    obj.workout_parts.add(workout_parts_obj)

                    print("---")

                obj.save()

            import_summary = {
                "created": created,
                "skipped": skipped,
                "total": len(workouts_data),
            }
            self.stdout.write(f"{fname}: {import_summary}")

        else:
            self.stdout.write(f"{fname}: missing")
