from django.db import models
from django.contrib.auth.models import User
from .choices import GENDER_CHOICES
from utils.utility import BaseModel

class AnimalCategory(BaseModel):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class AnimalBreed(BaseModel):
    breed = models.CharField(max_length=100)

    def __str__(self):
        return self.breed

class AnimalColor(BaseModel):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Animal(BaseModel):
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

    def incrementViews(self):
        self.views += 1
        self.save()

    def incrementLikes(self):
        self.likes += 1
        self.save()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class AnimalLocation(BaseModel):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_query_name='animal_location')
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.location} - {self.animal.name}'

class AnimalImages(BaseModel):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='animal_images')
    image = models.ImageField(upload_to='animals')

    def __str__(self):
        return f'image - {self.animal.name}'
