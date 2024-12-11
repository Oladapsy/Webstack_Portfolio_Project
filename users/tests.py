from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='john.doe', email='john.doe@example.com', password='password123', full_name="John Doe")

    def test_user_creation(self):
        user = CustomUser.objects.get(email="john.doe@example.com")
        self.assertEqual(user.full_name, "John Doe")

class UserSignupViewTest(APITestCase):
    def setUp(self):
        self.user_data = {
            'email': 'jane.doe@example.com',
            'full_name': 'Jane Doe',
            'username': 'jane.doe',  # Ensure to provide username
            'password': 'password123'
        }

    def test_user_signup(self):
        response = self.client.post(reverse('signup'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserLoginViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='john.doe', email='john.doe@example.com', password='password123', full_name='John Doe')
        self.login_data = {'email': 'john.doe@example.com', 'password': 'password123'}

    def test_user_login(self):
        response = self.client.post(reverse('login'), self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
