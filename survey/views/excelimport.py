from tablib import Dataset
from survey.resources import QuestionResource, SurveyResource

def question_upload(request):
    if request.method == 'POST':
        question_resource = QuestionResource()
        dataset = Dataset()
        new_questions = request.FILES['myfile']

        imported_data = dataset.load(new_questions.read())
        result = question_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            question_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'survey/import.html')

def survey_upload(request):
    if request.method == 'POST':
        survey_resource = SurveyResource()
        dataset = Dataset()
        new_surveys = request.FILES['myfile']

        imported_data = dataset.load(new_surveys.read())
        result = survey_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            survey_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'survey/import.html')