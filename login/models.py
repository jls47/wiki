from django.db import models

# Create your models here.

class login(models.Model):
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)