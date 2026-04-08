from django.db import models
from django.contrib.auth.models import User
from utils.utility import BaseModel

class Blog(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_paid = models.BooleanField(default=False)

class Subscription(BaseModel):
    title = models.CharField(max_length=100)
    validity = models.IntegerField(default=30)
    price = models.IntegerField()

class SubscriptionOrder(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    expiry = models.DateField()
    is_paid = models.BooleanField(default=False)