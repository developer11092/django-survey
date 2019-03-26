from .resources import SurveyResource, QuestionResource

def SurveyCSV(self):    
    survey_resource = SurveyResource()
    dataset = survey_resource.export()
    dataset.csv

def QuestionCSV(self):
    question_resource = QuestionResource()
    dataset = question_resource.export()
    dataset.csv