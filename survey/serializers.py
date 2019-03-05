from rest_framework import serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'description', 'is_published', 'need_logged_user', 'allows_multiple_interviews', 'company')

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         models = Question
#         fields = ('id', 'text', 'order', 'required', 'category', 'survey', 'type', 'choices')
