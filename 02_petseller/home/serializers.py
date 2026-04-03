from rest_framework import serializers
from .models import (AnimalCategory, AnimalBreed, AnimalColor, Animal, AnimalLocation, AnimalImages)

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
    animal_images = AnimalImagesSerializer(many=True)

    def get_category(self, obj):
        return obj.category.category
    
    class Meta:
        model = Animal
        exclude = ['updated_at']
        
        