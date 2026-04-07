from rest_framework import serializers
from .models import (AnimalCategory, AnimalBreed, AnimalColor, Animal, AnimalLocation, AnimalImages)
from django.contrib.auth.models import User
class AnimalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalCategory
        fields = '__all__'
        
class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreed
        fields = ['breed']
        
class AnimalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalColor
        fields = ['color']

class AnimalLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLocation
        fields = '__all__'
        
class AnimalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalImages
        fields = ['image']
        
class AnimalSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    color = AnimalColorSerializer(many=True)
    breed = AnimalBreedSerializer(many=True)
    # animal_images = AnimalImagesSerializer(many=True)

    def get_category(self, obj):
        return obj.category.category
    
    def create(self, data):
        breed = data.pop('breed')
        color = data.pop('color')
        animal = Animal.objects.create(**data, category=AnimalCategory.objects.get(category="DOG"))

        for b in breed:
            breed_obj, _ = AnimalBreed.objects.get_or_create(breed=b['breed'])
            animal.breed.add(breed_obj)
        for c in color:
            color_obj, _ = AnimalColor.objects.get_or_create(color=c['color'])
            animal.color.add(color_obj)

        return animal
    class Meta:
        model = Animal
        exclude = ['updated_at']

        

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if 'username' in data:
            user = User.objects.filter(username = data['username'])
            if user.exists():
                raise serializers.ValidationError('username is already taken')

        if 'email' in data:
            user = User.objects.filter(email = data['email'])
            if user.exists():
                raise serializers.ValidationError('email already exist')
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if 'username' in data:
            user = User.objects.filter(username=data['username'])
            if not user.exists():
                raise serializers.ValidationError('username does not exist')
        return data