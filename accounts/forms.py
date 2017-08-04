__author__ = 'Luke'

from django import forms
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextFormField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text = "Optional.")
    email = forms.EmailField(max_length=250, help_text="Email address required.")
    confirm_email = forms.EmailField(max_length=250, help_text="Confirm email address.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'confirm_email')