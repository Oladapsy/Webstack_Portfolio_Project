import uuid
from django.conf import settings
from django.db import models

class UnifiedModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invoices')

    # Common fields
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    # Invoice fields
    invoice_number = models.CharField(max_length=20, unique=True, editable=False)
    date_issued = models.DateField(auto_now_add=True)  # Use only auto_now_add
    due_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue')
    ], default='Pending')

    # Item fields
    item_title = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()
        super(UnifiedModel, self).save(*args, **kwargs)

    def generate_invoice_number(self):
        return f'INV-{uuid.uuid4().hex[:8].upper()}'

    def __str__(self):
        return self.name if self.name else f"Invoice {self.invoice_number}"

    @property
    def total_amount(self):
        return self.quantity * self.price if self.quantity and self.price else 0  # Corrected

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['invoice_number', 'item_title'], name='unique_invoice_item')
        ]
