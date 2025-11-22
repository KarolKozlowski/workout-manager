from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from wmapi.models import Workout


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
