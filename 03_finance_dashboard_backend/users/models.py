from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import ROLE_CHOICES

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'admin'
        super().save(*args, **kwargs)
