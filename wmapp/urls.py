from django.urls import path

from .views import IndexView, workout_detail

app_name = "wmapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("workout/<int:pk>/", workout_detail, name="workout_detail"),
]
