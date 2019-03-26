from django.http import HttpResponse
from survey.resources import SurveyResource, QuestionResource

def exportSurvey(request):
    survey_resource = SurveyResource()
    dataset = SurveyResource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="surveys.csv"'
    return response

def exportQuestion(request):
    question_resource = QuestionResource
    dataset = QuestionResource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="questions.csv"'
    return response