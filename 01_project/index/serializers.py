from rest_framework import serializers
from .models import (
    Form, Choices, Questions, Answers, Responses
)


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ['created_at', 'updated_at']
        
class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        exclude = ['created_at', 'updated_at']
        
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        exclude = ['created_at', 'updated_at']
        
class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        exclude = ['created_at', 'updated_at']
        
class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responses
        exclude = ['created_at', 'updated_at']
        