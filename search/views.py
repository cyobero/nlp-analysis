# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from search.forms import SearchForm
from natlang.views import classify_text

# Create your views here.
def search(request):
    # store any errors here
    errors = []
    # If request is a POST then we need to process the form data.
    if request.method == 'POST':
        # Create a form instance and populate it with data
        # from the request
        form = SearchForm(request.POST)
        # Check to see if form is valid
        if form.is_valid():
            # extract text from form
            text = form.cleaned_data['text']
            categories = classify_text(text).categories
            return render(request, 'search.html', {'form': form, 'categories': categories})

    # If request method is GET (or any other method) then
    # create a blank form.
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})