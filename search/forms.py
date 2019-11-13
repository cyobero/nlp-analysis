from django import forms
from search.models import TextCategories

class SearchForm(forms.ModelForm):
    class Meta:
        model = TextCategories
        widgets = {
            'text': forms.Textarea
        }
        fields = ['text']