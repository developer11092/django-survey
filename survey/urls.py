# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from survey.views import ConfirmView, IndexView, SurveyCompleted, SurveyDetail
from survey.views.serializerview import SurveyView #, QuestionView
from survey.views.survey_result import serve_result_csv
from rest_framework import routers
from survey.views.serializerview import LoginView, LogoutView

routers = routers.DefaultRouter()
routers.register('surveys', SurveyView)
# routers.register('questions', QuestionView)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='survey-list'),
    url(r'^(?P<id>\d+)/', SurveyDetail.as_view(), name='survey-detail'),
    url(r'^csv/(?P<primary_key>\d+)/', serve_result_csv, name='survey-result'),
    url(r'^(?P<id>\d+)/completed/', SurveyCompleted.as_view(),
        name='survey-completed'),
    url(r'^(?P<id>\d+)-(?P<step>\d+)/', SurveyDetail.as_view(),
        name='survey-detail-step'),
    url(r'^confirm/(?P<uuid>\w+)/', ConfirmView.as_view(),
        name='survey-confirmation'),
    url('api/', include(routers.urls)),
    url('api/login/', LoginView.as_view()),
    url('api/logout/', LogoutView.as_view()),
]
