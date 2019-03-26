from django.http import HttpResponse
from survey.resources import SurveyResource, QuestionResource

def exportSurvey(request):
    survey_resource = SurveyResource()
    dataset = SurveyResource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="surveys.json"'
    return response

def exportQuestion(request):
    question_resource = QuestionResource
    dataset = QuestionResource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="questions.json"'
    return response