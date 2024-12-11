from django.test import TestCase
from .models import Client, Invoice, Item
from django.utils import timezone


# Create your tests here.

class ClientModelTest(TestCase):
    def setUp(self):
        Client.objects.create(name="John Doe", email="john.doe@example.com", address="123 Elm Street")

    def test_client_creation(self):
        client = Client.objects.get(name="John Doe")
        self.assertEqual(client.email, "john.doe@example.com")
        self.assertEqual(client.address, "123 Elm Street")

class InvoiceModelTest(TestCase):
    def setUp(self):
        client = Client.objects.create(name="Jane Smith", email="jane.smith@example.com", address="456 Oak Street")
        Invoice.objects.create(client=client, invoice_number="INV001", due_date=timezone.now())

    def test_invoice_creation(self):
        invoice = Invoice.objects.get(invoice_number="INV001")
        self.assertEqual(invoice.client.name, "Jane Smith")

class ItemModelTest(TestCase):
    def setUp(self):
        client = Client.objects.create(name="John Doe", email="john.doe@example.com", address="123 Elm Street")
        invoice = Invoice.objects.create(client=client, invoice_number="INV002", due_date=timezone.now())
        Item.objects.create(invoice=invoice, title="Widget", quantity=10, price=5.00)

    def test_item_creation(self):
        item = Item.objects.get(title="Widget")
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.price, 5.00)
