from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=600)
    toc = models.CharField(max_length=600)
    body = models.TextField(max_length=10000000)
    categories = models.CharField(max_length=600)
    featured = models.BooleanField(default=False)

class Talk(models.Model):
    discussions = models.TextField(max_length=9999999999999999999)

    def __str__(self):
        return self.title





