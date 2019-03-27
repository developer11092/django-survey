# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from company.models import Company
# from .question import Question


try:
    from django.conf import settings
    if settings.AUTH_USER_MODEL:
        user_model = settings.AUTH_USER_MODEL
    else:
        user_model = User
except (ImportError, AttributeError):
    user_model = User

class Survey(models.Model):

    name = models.CharField(_("Name"), max_length=400)
    description = models.TextField(_("Description"), )
    is_published = models.BooleanField(_("Users can see it and answer it"),)
    need_logged_user = models.BooleanField(_("Only authenticated users can see it and answer it"),)
    display_by_question = models.BooleanField(_("Display by question"),)
    # template = models.CharField(_("Template"), max_length=255, null=True, blank=True)
    allows_multiple_interviews = models.BooleanField(verbose_name=_("Allows multiple interviews"),
                                                     blank=True, default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                               verbose_name=_("company"),
                               related_name="surveys",
                               null=True)
    class Meta(object):
        verbose_name = _('survey')
        verbose_name_plural = _('surveys')

    def __str__(self):
        return self.name

    def latest_answer_date(self):
        """ Return the latest answer date.

        Return None is there is no response. """
        min_ = None
        for response in self.responses.all():
            if min_ is None or min_ < response.updated:
                min_ = response.updated
        return min_

    def get_absolute_url(self):
        return reverse('survey-detail', kwargs={"id": self.pk})

    @property
    def interview_count(self):
        # NOTSURE: Do we realy need this optimisation?
        if hasattr(self, '_interview_count'):
            return self._interview_count
        self._interview_count = len(Answer.objects.filter(
            question__survey=self.id).values('interview_uuid').distinct())
        return self._interview_count

    @property
    def session_key_count(self):
        # NOTSURE: Do we realy need this optimisation?
        if hasattr(self, '_session_key_count'):
            return self._submission_count
        self._submission_count = len(Answer.objects.filter(
            question__survey=self.id).values('session_key').distinct())
        return self._submission_count

    @property
    def questions(self):
        return self.question_set.all()