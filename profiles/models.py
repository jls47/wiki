from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    summary = RichTextField(max_length=600)
    edited = models.CharField(max_length=600)
    created = models.CharField(max_length=600)

