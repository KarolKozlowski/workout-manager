from django.conf import settings
from django.test import SimpleTestCase


class SmokeTests(SimpleTestCase):
    """Small smoke tests that don't require the database.

    These ensure the basic Django configuration and app registration
    are present so CI has a simple assertion to run.
    """

    def test_wmapp_is_installed(self):
        assert "wmapp" in settings.INSTALLED_APPS

    def test_debug_setting_exists(self):
        # Ensure DEBUG exists and is a boolean-like value
        assert hasattr(settings, "DEBUG")
