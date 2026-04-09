from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class RecordTest(APITestCase):

    def setUp(self):
        # Create admin user
        self.user = User.objects.create_user(
            username="admin",
            password="1234",
            role="admin"
        )

        # Login
        response = self.client.post("/api/token/", {
            "username": "admin",
            "password": "1234"
        })

        self.token = response.data["access"]

    def test_create_record(self):
        url = "/records/"

        data = {
            "amount": 1000,
            "type": "income",
            "category": "salary",
            "date": "2026-04-06",
            "notes": "test"
        }

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # 🔥 Test 3: Get Records
    def test_get_records(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        response = self.client.get("/records/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 🔥 Test 4: Viewer cannot create record
    def test_viewer_cannot_create_record(self):
        # Create viewer user
        viewer = User.objects.create_user(
            username="viewer",
            password="1234",
            role="viewer"
        )

        # Login as viewer
        response = self.client.post("/api/token/", {
            "username": "viewer",
            "password": "1234"
        })

        viewer_token = response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {viewer_token}"
        )

        response = self.client.post("/records/", {
            "amount": 1000,
            "type": "income",
            "category": "salary",
            "date": "2026-04-06",
            "notes": "test"
        })

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)