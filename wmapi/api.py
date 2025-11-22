from rest_framework import permissions, viewsets

from wmapi.models import (
    BodyPart,
    Equipment,
    Exercise,
    ExerciseInstance,
    Muscle,
    Set,
    Workout,
    WorkoutDay,
    WorkoutPart,
)

from .serializers import (
    BodyPartSerializer,
    EquipmentSerializer,
    ExerciseInstanceSerializer,
    ExerciseSerializer,
    MuscleSerializer,
    SetSerializer,
    WorkoutDaySerializer,
    WorkoutPartSerializer,
    WorkoutSerializer,
)


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.AllowAny]


class WorkoutPartViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPart.objects.all()
    serializer_class = WorkoutPartSerializer
    permission_classes = [permissions.AllowAny]


class WorkoutDayViewSet(viewsets.ModelViewSet):
    queryset = WorkoutDay.objects.all()
    serializer_class = WorkoutDaySerializer
    permission_classes = [permissions.AllowAny]


class ExerciseInstanceViewSet(viewsets.ModelViewSet):
    queryset = ExerciseInstance.objects.all()
    serializer_class = ExerciseInstanceSerializer
    permission_classes = [permissions.AllowAny]


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    permission_classes = [permissions.AllowAny]


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.AllowAny]


class BodyPartViewSet(viewsets.ModelViewSet):
    queryset = BodyPart.objects.all()
    serializer_class = BodyPartSerializer
    permission_classes = [permissions.AllowAny]


class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    permission_classes = [permissions.AllowAny]


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.AllowAny]
