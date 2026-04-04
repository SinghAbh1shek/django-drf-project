from django.db import models
from django.contrib.auth import get_user_model
from utils.utility import BaseModel
from .choices import TYPE_CHOICES

User = get_user_model()

class Category(BaseModel):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.category

class Record(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category_record')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_record')

    def __str__(self):
        return f'{self.type} - {self.created_by.username}'