from django.db import models
# from survey.models.survey import Survey
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


try:
    from django.conf import settings
    if settings.AUTH_USER_MODEL:
        user_model = settings.AUTH_USER_MODEL
    else:
        user_model = User
except (ImportError, AttributeError):
    user_model = User

class Company(models.Model):
    website = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    phonenumber = models.CharField(max_length = 100)
    # survey = models.ForeignKey(Survey, on_delete=models.CASCADE,
    #                            verbose_name=_("Survey"),
    #                            related_name="companies")
    user = models.ForeignKey(user_model, on_delete=models.SET_NULL,
                             verbose_name=_("User"), null=True,
                             blank=True)

    class Meta:
        db_table = "company"

    class Meta(object):
        verbose_name = _('company')
        verbose_name_plural = _('companies')

    def __str__(self):
        return self.name

class Online(models.Model):
    domain = models.CharField(max_length = 30)
   
    class Meta:
        db_table = "online"

