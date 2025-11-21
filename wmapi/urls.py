from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import WorkoutViewSet

router = DefaultRouter()
router.register(r"workouts", WorkoutViewSet, basename="workout")

# Expose the router at the app root. The project URL config will mount
# this app under `/api/v1/`.
urlpatterns = [
    path("", include((router.urls, "api"), namespace="api")),
]
