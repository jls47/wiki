from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    summary = RichTextField('Summary')
    body = RichTextField('Body')
    categories = models.CharField(max_length=600)
    featured = models.BooleanField(default=False)

class Talk(models.Model):
    discussions = models.TextField(max_length=9999999999999999999)

    def __str__(self):
        return self.title





