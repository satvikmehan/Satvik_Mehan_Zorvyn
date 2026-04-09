from rest_framework.test import APITestCase
from users.models import User


class DashboardTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="user",
            password="1234"
        )

        response = self.client.post("/api/token/", {
            "username": "user",
            "password": "1234"
        })

        self.token = response.data["access"]

    def test_summary(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        response = self.client.get("/dashboard/summary/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.data)