from django.db import models
from django.utils.translation import gettext as _


class Workout(models.Model):
    """A simple Workout model for CRUD via the API.

    Fields are intentionally minimal for a smoke API and can be
    expanded later.
    """

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    duration_minutes = models.PositiveIntegerField(null=True, blank=True)

    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)

    workout_parts = models.ManyToManyField("wmapi.WorkoutPart", blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start_datetime", "-end_datetime"]
        # Keep the model attached to the original `wmapp` app label so
        # existing migrations and DB tables remain valid after moving
        # the code into the `wmapi` package.
        app_label = "wmapi"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class WorkoutPart(models.Model):
    """Model for parts of a workout (e.g., warmup, strength, cardio)."""

    class PartName(models.TextChoices):
        """Enum for workout part names."""

        WARMUP = _("Warmup")
        STRENGTH = _("Strength")
        STRETCHING = _("Stretching")
        CARDIO = _("Cardio")

    type = models.CharField(max_length=50, choices=PartName.choices)

    exercises = models.ManyToManyField("wmapi.ExerciseInstance", blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "wmapi"

    def __str__(self) -> str:  # pragma: no cover - trivial
        exercises = ", ".join(str(v.exercise_id) for v in self.exercises.all())
        return f"{self.type}: {exercises}"


class ExerciseInstance(models.Model):
    """Model for an instance of an exercise within a workout."""

    exercise_id = models.ForeignKey(
        "wmapi.Exercise", on_delete=models.PROTECT, related_name="instances"
    )
    sets = models.ManyToManyField("wmapi.Set", blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "wmapi"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.exercise_id.name} {self.exercise_id.id}"


class Set(models.Model):
    """Model for a set within an exercise instance."""

    repetitions = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    rest_seconds = models.PositiveIntegerField(null=True, blank=True)

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "wmapi"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"Set: {self.repetitions} {_('reps')}, {self.weight} kg, {self.rest_seconds} {_('sec rest')}"


# --- the below models are compatible with exercisedb API --- #


class Exercise(models.Model):
    """An Exercise model."""

    name = models.CharField(max_length=200)
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    external_link = models.URLField(blank=True, null=True)

    overview = models.TextField(blank=True, null=True)
    keywords = models.JSONField(default=list, blank=True)
    exercise_tips = models.JSONField(default=list, blank=True)
    variations = models.TextField(blank=True, null=True)
    # TODO: type mapping
    related_exercise_ids = models.JSONField(default=list, blank=True)

    instructions = models.JSONField(default=list, blank=True)

    # many-to-many relationships to lookup models
    # TODO: type mapping
    exercise_type = models.CharField(max_length=100, blank=True, null=True)
    target_muscles = models.ManyToManyField("wmapi.Muscle")
    body_parts = models.ManyToManyField("wmapi.BodyPart")
    equipments = models.ManyToManyField("wmapi.Equipment")
    secondary_muscles = models.ManyToManyField(
        "wmapi.Muscle", related_name="secondary_exercises"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "wmapi"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class BodyPart(models.Model):
    """Simple lookup model for exercise body parts.

    This was previously stored as free-form strings in the
    `Exercise.body_parts` JSONField. Having a dedicated model makes it
    easier to manage canonical values and to populate from a JSON file.
    """

    name = models.CharField(max_length=200, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "wmapi"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class Muscle(models.Model):
    """Lookup model for muscles/targets used in exercises."""

    name = models.CharField(max_length=200, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "wmapi"
        ordering = ["name"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class Equipment(models.Model):
    """Lookup model for exercise equipments."""

    name = models.CharField(max_length=200, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "wmapi"
        ordering = ["name"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name
