from django.db import models


class Workout(models.Model):
    """A simple Workout model for CRUD via the API.

    Fields are intentionally minimal for a smoke API and can be
    expanded later.
    """

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    performed_at = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-performed_at", "-created_at"]
        # Keep the model attached to the original `wmapp` app label so
        # existing migrations and DB tables remain valid after moving
        # the code into the `wmapi` package.
        app_label = "wmapi"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class Exercise(models.Model):
    """A simple Workout model for CRUD via the API.

    Fields are intentionally minimal for a smoke API and can be
    expanded later.
    """

    name = models.CharField(max_length=200)
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

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
