# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sentiment(models.Model):
    text = models.TextField()
    score = models.FloatField()
    magnitude = models.FloatField()