from django.db import models

# Create your models here.

class profile(models.Model):
    summary = models.TextField(max_length=600)
    edited = models.CharField(max_length=600)
    created = models.CharField(max_length=600)

