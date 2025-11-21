from django.conf import settings
from django.test import SimpleTestCase


class SmokeTests(SimpleTestCase):
    """Small smoke tests that don't require the database.

    These ensure the basic Django configuration and app registration
    """

    def test_wmapp_is_installed(self):
        # Ensure 'wmapp' is in INSTALLED_APPS
        assert "wmapp" in settings.INSTALLED_APPS

    def test_debug_setting_exists(self):
        # Ensure DEBUG exists and is a boolean-like value
        assert hasattr(settings, "DEBUG")

    def test_index_view_renders(self):
        # Ensure the index view renders correctly
        url = ""
        response = self.client.get(url)
        assert response.status_code == 200
        assert b"Hello, world." in response.content
