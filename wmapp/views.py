from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Simple index view for the app.

    Uses a template so it's easy to extend with HTML later.
    """

    template_name = "wmapp/index.html"
