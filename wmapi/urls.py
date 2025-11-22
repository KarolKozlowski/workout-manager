from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import (
    BodyPartViewSet,
    EquipmentViewSet,
    ExerciseInstanceViewSet,
    ExerciseViewSet,
    MuscleViewSet,
    SetViewSet,
    WorkoutPartViewSet,
    WorkoutViewSet,
)

router = DefaultRouter()
router.register(r"workouts", WorkoutViewSet, basename="workout")

router.register(r"workoutparts", WorkoutPartViewSet, basename="workoutpart")
router.register(
    r"exerciseinstances", ExerciseInstanceViewSet, basename="exerciseinstance"
)
router.register(r"sets", SetViewSet, basename="set")

router.register(r"exercises", ExerciseViewSet, basename="exercise")
router.register(r"bodyparts", BodyPartViewSet, basename="bodypart")
router.register(r"muscles", MuscleViewSet, basename="muscle")
router.register(r"equipments", EquipmentViewSet, basename="equipment")


# Expose the router at the app root. The project URL config will mount
# this app under `/api/v1/`.
urlpatterns = [
    path("", include((router.urls, "api"), namespace="api")),
]
