__author__ = 'Luke'
from django import forms
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextFormField
from .models import Article

class ArtModelForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = ('title', 'slug', 'summary', 'body', 'categories',)
        model.body = RichTextField()