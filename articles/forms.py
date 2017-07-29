__author__ = 'Luke'
from django import forms

from .models import Article

class ArtModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'