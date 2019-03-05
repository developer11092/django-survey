from django.shortcuts import render
from rest_framework import viewsets
from survey.models import Survey
from survey.serializers import SurveySerializer# , QuestionSerializer

class SurveyView(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

# class QuestionView(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer