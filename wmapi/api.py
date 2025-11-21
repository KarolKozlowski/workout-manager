from rest_framework import permissions, viewsets

from wmapi.models import Workout

from .serializers import WorkoutSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.AllowAny]
