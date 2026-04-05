from rest_framework import serializers
from .models import Record, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):

    category = serializers.CharField(write_only=True)
    category_name = serializers.SerializerMethodField()
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Record
        fields = [
            'id',
            'amount',
            'type',
            'date',
            'notes',
            'is_deleted',
            'category',
            'category_name',
            'created_by',
            'created_at',
        ]
    def get_category_name(self, obj):
        return obj.category.category
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value
    
    def create(self, validated_data):
        category_name = validated_data.pop('category').strip().lower() # popped category name form the data and normalized case sensitivity
        type = validated_data['type']

        category, _ = Category.objects.get_or_create(category=category_name, type=type)
        validated_data['category'] = category
        return Record.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        category_name = validated_data.pop('category', None)
        if category_name:
            category_name = category_name.strip().lower()
            type = validated_data.get('type', instance.type)
            category, _ = Category.objects.get_or_create(category=category_name, type=type)
            instance.category = category

        # dynamically updating other data exept category
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
