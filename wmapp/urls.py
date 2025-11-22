from django.urls import path

from .views import IndexView, exercise_detail, workout_detail, workouts_list

app_name = "wmapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("workout/<int:pk>/", workout_detail, name="workout_detail"),
    path("workouts/", workouts_list, name="workouts_list"),
    path("exercise/<int:pk>/", exercise_detail, name="exercise_detail"),
]
