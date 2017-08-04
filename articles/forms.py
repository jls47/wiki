__author__ = 'Luke'
from django import forms
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextFormField
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArtModelForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = ('title', 'slug', 'summary', 'body', 'categories',)
        model.body = RichTextField()

