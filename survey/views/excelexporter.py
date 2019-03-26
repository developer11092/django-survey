from django.http import HttpResponse
from survey.resources import SurveyResource, QuestionResource

def exportSurvey(request):
    survey_resource = SurveyResource()
    dataset = SurveyResource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="surveys.xls"'
    return response

def exportQuestion(request):
    question_resource = QuestionResource
    dataset = QuestionResource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="questions.xls"'
    return response