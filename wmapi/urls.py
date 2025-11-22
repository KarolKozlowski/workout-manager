from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import (
    BodyPartViewSet,
    EquipmentViewSet,
    ExerciseViewSet,
    MuscleViewSet,
    WorkoutViewSet,
)

router = DefaultRouter()
router.register(r"exercises", ExerciseViewSet, basename="exercise")
router.register(r"bodyparts", BodyPartViewSet, basename="bodypart")
router.register(r"muscles", MuscleViewSet, basename="muscle")
router.register(r"equipments", EquipmentViewSet, basename="equipment")

router.register(r"workouts", WorkoutViewSet, basename="workout")
# Expose the router at the app root. The project URL config will mount
# this app under `/api/v1/`.
urlpatterns = [
    path("", include((router.urls, "api"), namespace="api")),
]
