from django.db import models

# Create your models here.
class Client(models.Model):
    """model for the user or client"""
    company_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.company_name} ({self.email})"

class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20, unique=True)
    date_issued = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    STATUS_CHOICES = [
        ('Pending', 'pending'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client.company_name}"

    @property
    def total_amount(self):
        """calculate the total amount from related items"""
        return sum(item.total_price for item in self.items.all())

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def total_price(self):
        """calculate total price of item"""
        return self.quantity * self.price

    def __str__(self):
        return f"{self.title} (x{self.quantity}) - {self.total_price}"
    
