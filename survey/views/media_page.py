#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from builtins import super
import logging

from django.views.generic import TemplateView
from survey.models import Question



class MediaPage(TemplateView):

    template_name = 'survey/survey.html'
    
    def get_context_data(self, **kwargs):
        context = super(MediaPage, self).get_context_data(**kwargs)
        Question = Question.objects.all()
        logging.debug(Question)
        return context