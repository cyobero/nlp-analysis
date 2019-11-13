# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from natlang.views import sentiment
from search.forms import SearchForm


# Create your views here.
def get_sentiment(request):
    # store any errors here
    # If request is a POST then we need to process the form data.
    if request.method == 'POST':
        # Create a form instance and populate it with data
        # from the request
        form = SearchForm(request.POST)
        # Check to see if form is valid
        if form.is_valid():
            # extract text from form
            text = form.cleaned_data['text']
            results = sentiment(text)
            return render(request, 'search-sentiment.html', {'form': form, 'results': results})

    # If request method is GET (or any other method) then
    # create a blank form.
    else:
        form = SearchForm()

    return render(request, 'search-sentiment.html', {'form': form})