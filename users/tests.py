from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class SignupTest(APITestCase):

    def test_signup(self):
        url = "/signup/"

        data = {
            "username": "testuser",
            "email": "test@test.com",
            "password": "1234"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="1234"
        )

    def test_login(self):
        response = self.client.post("/api/token/", {
            "username": "testuser",
            "password": "1234"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)