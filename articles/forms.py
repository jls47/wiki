__author__ = 'Luke'
from django import forms
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextFormField
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import format_lazy, slugify
from django.utils.translation import pgettext_lazy



class ArtModelForm(forms.ModelForm):
    class Meta:
        model = Article
        #form fields the user can actually use
        fields = ('title', 'summary', 'body', 'category',)
        model.body = RichTextField()
        model.author = User.username
        model.slug = slugify(model.title)


    def save(self):
        instance = super(ArtModelForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.author = str(User.username)
        instance.save()

        return instance

