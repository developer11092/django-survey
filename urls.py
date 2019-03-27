# -*- coding: utf-8 -*-

# pylint: disable=invalid-name

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib import auth
from django.shortcuts import redirect
from django.urls.base import reverse
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def home(request):
    """ Permit to not get 404 while testing. """
    return redirect(reverse("survey-list"))


urlpatterns = [
    # url(r"^$", home, name="home"),
    # url('accounts/', include('django.contrib.auth.urls')),
    # url(r'^rosetta/', include('rosetta.urls')),
    url('survey/', include('survey.urls')),
    url(r'^admin/', admin.site.urls),
    # url('', admin.site.urls),
    # url('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)