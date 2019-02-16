from django.db import models
from builtins import super
import logging

from django.db import models
from django.db.models import Count
from random import randint
from django.utils.translation import ugettext_lazy as _

class VideoCategory(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(_("Creation time"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated time"), auto_now_add=True)

    class Meta(object):
        verbose_name = _('videocategory')
        verbose_name_plural = _('videocategories')

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(_("Name of the video"), max_length=100, default="Music Video")
    vid =  models.CharField(_("Video ID"), blank=True, null=False, max_length=50, unique=True)
    url =  models.CharField(_("Link to the video"),max_length=255, null=True, blank=True)
    type = models.IntegerField(_("Player"),default=0) # 0: youtube, 1: others
    cat = models.ForeignKey(VideoCategory,
                           on_delete=models.CASCADE,
                           verbose_name=_("videocategory"),
                           related_name="videos",
                           default=1)
    start = models.CharField(_("Start time"),max_length=10)
    end = models.CharField(_("End time"), max_length=10)
    created = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_("Update date"), auto_now=True)


    class Meta(object):
        verbose_name = _('video')
        verbose_name_plural = _('videos')

    def __str__(self):
        return self.name
