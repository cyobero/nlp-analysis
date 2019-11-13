# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Create your views here.
def classify_text(text):
    # If GOOGLE_APPLICATION_CREDENTIALS isn't set in local
    # environment then generate an API key and pass it through
    # LanguageServiceClient(credentials=API_KEY).
    client = language.LanguageServiceClient()
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    categories = client.classify_text(document=document)
    return categories


def sentiment(text):
    client = language.LanguageServiceClient()
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    results = client.analyze_sentiment(document).document_sentiment
    return results