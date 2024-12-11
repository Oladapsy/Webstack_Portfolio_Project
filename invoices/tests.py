from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import CustomUser
from .models import UnifiedModel

class UnifiedModelTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='john.doe', email='john.doe@example.com', password='password123', full_name='John Doe')
        self.client.force_authenticate(user=self.user)
        self.data = {
            "name": "Jane Doe",
            "email": "jane.doe@example.com",
            "address": "123 Elm Street",
            "phone_number": "123-456-7890",
            "item_title": "Widget",
            "quantity": 10,
            "price": 5.00,
            "date_issued": "2023-12-15",
            "due_date": "2024-01-15",
            "description": "Consulting Services",
            "status": "Pending"
        }

    def test_invoice_creation(self):
        response = self.client.post(reverse('unifiedmodel-list'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user.username)

    def test_total_amount_calculation(self):
        unified_instance = UnifiedModel.objects.create(user=self.user, **self.data)
        self.assertEqual(unified_instance.total_amount, 50.00)
