from django import forms
from django.forms import fields
from .models import DictionaryDb

class DictionaryForm(forms.ModelForm):
    class Meta:
        model=DictionaryDb
        fields= ['word', 'letter', 'definition','example']