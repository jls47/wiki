from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import format_lazy, slugify
from django.utils.translation import pgettext_lazy
from random import randint
from django.db.models.aggregates import Count


# Create your models here.
class Article(models.Model): #All the areas of input that are possible.
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = RichTextField('Summary') # django safe filter
    body = RichTextField('Body')
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length = 100)
    featured = models.BooleanField(default=False)
    pastFeatured = models.BooleanField(default=False)
    author = models.CharField(max_length=120)
    editedby = models.CharField(max_length=999999999999)
    editedtime = models.CharField(max_length=999999999999)

class Talk(models.Model):
    discussions = RichTextField()

    def __str__(self):
        return self.title

class RandomArt(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('slug'))['count']
        random_index = randint(0, count-1)
        print(self.all()[random_index])
        return self.all()[random_index]





