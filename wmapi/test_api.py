from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient

from wmapi.models import Workout


class WorkoutAPITests(TestCase):
    def test_wmapp_is_installed(self):
        # Ensure 'wmapi' is in INSTALLED_APPS
        assert "wmapi" in settings.INSTALLED_APPS

    def setUp(self):
        self.client = APIClient()

    def test_crud_workout(self):
        # Create
        url = "/api/v1/workouts/"
        data = {"name": "Morning Run", "duration_minutes": 30}
        resp = self.client.post(url, data, format="json")
        assert resp.status_code == 201
        wid = resp.data["id"]

        # Retrieve
        resp = self.client.get(f"{url}{wid}/")
        assert resp.status_code == 200
        assert resp.data["name"] == "Morning Run"

        # Update
        resp = self.client.patch(
            f"{url}{wid}/", {"duration_minutes": 45}, format="json"
        )
        assert resp.status_code == 200
        assert resp.data["duration_minutes"] == 45

        # List
        resp = self.client.get(url)
        assert resp.status_code == 200
        assert any(w["id"] == wid for w in resp.data)

        # Delete
        resp = self.client.delete(f"{url}{wid}/")
        assert resp.status_code == 204
        assert not Workout.objects.filter(id=wid).exists()
