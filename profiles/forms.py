__author__ = 'Luke'
from django import forms
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextFormField
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import format_lazy, slugify
from django.utils.translation import pgettext_lazy



class ProfModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        #form fields the user can actually use
        fields = ('summary',)


    def save(self):
        instance = super(ProfModelForm, self).save(commit=False)
        instance.save()

        return instance

