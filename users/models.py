from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return f'{self.email} - {self.full_name}'