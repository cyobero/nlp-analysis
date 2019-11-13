# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from sentiment.models import Sentiment

class SentimentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sentiment, SentimentAdmin)