from django.db import models
from django.contrib.auth.models import User
from .choices import GENDER_CHOICES

class AnimalCategory(models.Model):
    category = models.CharField(max_length=100)

class AnimalBreed(models.Model):
    breed = models.CharField(max_length=100)

class AnimalColor(models.Model):
    color = models.CharField(max_length=100)

class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animal')
    category = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE, related_name='animal_category')
    name = models.CharField(max_length=100)
    description = models.TextField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=1)
    slug = models.SlugField(max_length=1000, unique= True)
    breed = models.ManyToManyField(AnimalBreed, null=True)
    color = models.ManyToManyField(AnimalColor, null=True)

class AnimalLocation(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_query_name='animal_location')
    location = models.CharField(max_length=100)

class AnimalImages(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='animal_images')
    image = models.ImageField(upload_to='animals')
