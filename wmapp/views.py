from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from wmapi.models import Exercise, Workout


class IndexView(TemplateView):
    """Simple index view for the app.

    Uses a template so it's easy to extend with HTML later.
    """

    template_name = "wmapp/index.html"


def workout_detail(request, pk):
    """Load a `Workout` and render a page showing its children.

    The view prefetches related objects for reasonable performance.
    """
    qs = Workout.objects.prefetch_related(
        "workout_parts",
        "workout_parts__exercises",
        "workout_parts__exercises__exercise_id",
        "workout_parts__exercises__sets",
    )
    workout = get_object_or_404(qs, pk=pk)

    return render(request, "wmapp/workout_detail.html", {"workout": workout})


def workouts_list(request):
    """Render a page listing all Workouts with links to details."""
    qs = Workout.objects.prefetch_related(
        "workout_parts",
        "workout_parts__exercises",
        "workout_parts__exercises__exercise_id",
    )
    workouts = qs.all()

    return render(request, "wmapp/workouts_list.html", {"workouts": workouts})


def exercise_detail(request, pk):
    """Render details for a single Exercise (lookup from `wmapi.Exercise`).

    Prefetch related lookup tables and instances for display.
    """
    qs = Exercise.objects.prefetch_related(
        "target_muscles",
        "secondary_muscles",
        "body_parts",
        "equipments",
        "instances__sets",
    )
    exercise = get_object_or_404(qs, pk=pk)

    return render(request, "wmapp/exercise_detail.html", {"exercise": exercise})
