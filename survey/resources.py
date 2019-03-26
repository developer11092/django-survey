from import_export import resources
from .models import Answer, Category, Question, Response, Survey

class SurveyResource(resources.ModelResource):
    class Meta:
        model = Survey

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question