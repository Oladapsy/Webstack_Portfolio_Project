from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser

class UserSignupAPITest(APITestCase):
    def test_user_signup_success(self):
        """Test successful signup."""
        signup_data = {
            "full_name": "Jane Doe",
            "email": "jane.doe@example.com",
            "password": "password123",
            "company_name": "Doe Inc.",
            "logo": None
        }
        response = self.client.post(reverse('signup'), signup_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "User created successfully")

    def test_user_signup_failure(self):
        """Test signup with invalid data."""
        # Missing required fields
        signup_data = {
            "email": "",
            "password": "password123"
        }
        response = self.client.post(reverse('signup'), signup_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)  # Ensure email error is returned
