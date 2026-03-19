from rest_framework import serializers
from .models import (
    Form, Choices, Questions, Answers, Responses
)


class Form(serializers.ModelField):
    class Meta:
        model = Form
        exclude = ['created_at', 'updated_at']
        
class Choices(serializers.ModelField):
    class Meta:
        model = Choices
        exclude = ['created_at', 'updated_at']
        
class Questions(serializers.ModelField):
    class Meta:
        model = Questions
        exclude = ['created_at', 'updated_at']
        
class Answers(serializers.ModelField):
    class Meta:
        model = Answers
        exclude = ['created_at', 'updated_at']
        
class Responses(serializers.ModelField):
    class Meta:
        model = Responses
        exclude = ['created_at', 'updated_at']
        