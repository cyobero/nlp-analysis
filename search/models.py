# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class TextCategories(models.Model):
    text = models.TextField()
    categories = models.TextField()
