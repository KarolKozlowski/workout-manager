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
