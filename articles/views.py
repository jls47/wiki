from django.shortcuts import render
from django import forms
from .forms import ArtModelForm, ArtEditForm
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.http import HttpResponseRedirect
import operator
from django.db.models import Q
from articles.models import Article, RandomArt
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from profiles.models import Profile
import random

#This is where just about everything happens for articles.  Here, all requests are routed to the proper html file and the proper db requests are made to populate the pages.

def artabout(request):
    return render(request, 'articles/about.html') #This is returning the about.html thingy.

def get_all_articles(request):
    articles = Article.objects.all() #This is returning every existing article object from the database so that the user can see what's there.

    return render(request, 'articles/seeall.html', {"articles": articles, "title": "All Articles"})

def get_one_article(request, slug):
    articles = Article.objects.get(slug=slug)  #Returning an article based on a criteria of a slug.  A slug is a title in lowercase with dashes instead of spaces in this case, that can be used as a url parameter.
    catArticles = Article.objects.filter(category=articles.category)
    sub = articles.subcategory
    subCatArticles = Article.objects.filter(subcategory=sub)
    return render(request, 'articles/articleview.html', {"article": articles, "cats": catArticles, "subCats": subCatArticles})

def get_talk_page(request, slug):
    #talk = Talk.objects.get(slug=slug)  #Ditto, basically a forum page type thing.

    return render(request, 'articles/talk.html')

def get_write_page(request):  # How to write an article!  This presents authenticated users with a series of forms that represent different sections of an article.
    # if this is a POST request we need to process the form data that's there and send it off.
    if request.method == "POST":
        # create a form instance and populate it with data from the request in the backend.  This is not visible to the user and happens in the blink of an eye.
        form = ArtModelForm(request.POST)
        if form.is_valid():
            # check whether it's valid.  If so, then send everything off, and set the author field to the current user's username.
            form.author = User.username
            model_instance = form.save()
            model_instance.timestamp = timezone.now()
            model_instance.category = model_instance.category.lower()
            model_instance.subcategory = model_instance.subcategory.lower()
            model_instance.author = request.user.username #add the current user's username to the author field
            model_instance.save() #send the data to the database.  the article is created!
            profile = Profile.objects.get(name = model_instance.author)
            profile.created += ( " '" + model_instance.title + "', ")
            profile.save()
            print("Page written!  Check it out!")

            return HttpResponseRedirect('/articles/single/%s' % model_instance.slug)  #going to the newly created article!
    else:
         # if a GET (or any other method) we'll create a blank form series for the user to populate.
         article = Article.objects.get(slug='your-title-here')
         form = ArtModelForm(initial={'title': article.title, 'summary': article.summary, 'body': article.body, 'category': article.category, 'subcategory': article.subcategory}) #grabbing the forms
    return render(request, "articles/write.html", {'form': form})

def get_edit_page(request, slug): # a doozy.  This is the edit function.  It works similarly to the create page function, except for the fact that it pulls from existing material.
        article = Article.objects.get(slug = slug) #article object
        if request.method == 'POST':
            form = ArtEditForm(request.POST, instance=article)
            author = article.author
            if form.is_valid():
                model_instance = form.save()
                model_instance.author = author
                model_instance.timestamp = timezone.now()
                model_instance.editedtime += str(timezone.now()) #With this and the editedby field, admins should be able to track who edited what at what time
                model_instance.editedby = request.user.username #add the current user's username into the edited by field
                model_instance.save()
                cuser = request.user
                profile = Profile.objects.get(name = cuser.username)
                if model_instance.title in profile.edited:
                    pass
                else:
                    profile.edited += ( " '" + model_instance.title + "', ")
                print(profile.edited)
                profile.save()
                return HttpResponseRedirect('/articles/single/%s' % slug)
        else:
            # Creating a populated series of forms for users to monkey with.
            article = Article.objects.get(slug=slug)  #Selecting the article based on slug
            form = ArtEditForm(initial={'summary': article.summary, 'body': article.body})
            return render(request, "articles/edit.html", {'form': form}) #showing the forms


def get_categories(request, category):  #organizing things categorically
    articles = Article.objects.filter(category=category)
    sub = set([a.subcategory for a in articles])
    return render(request, 'articles/categories.html', {"articles": articles, "sub": sub})

def get_subcategories(request, subcategory):  #organizing things categorically
    articles = Article.objects.filter(subcategory=subcategory)

    return render(request, 'articles/subcategories.html', {"articles": articles})



def get_featured_articles(request):  #Articles that have been featured before
    articles = Article.objects.filter(pastfeatured=True)

    return render(request, 'articles/seeall.html', {"articles": articles, "title": "Featured"})

def get_front_page(request): #Article featured right now, with a list of categories to browse
    farticle = Article.objects.get(featured = True) #Can only be determined by someone with admin access.  Were this a bigger site, it might be up for a vote or something.
    articles = Article.objects.all()

    categories = set([a.category for a in articles])
    print(categories)
    return render(request, 'articles/frontpage.html', {"farticle": farticle, "categories": categories})

def get_search(request): #Searching the db for articles
    paginate_by = 10


    if request.method == "GET":
       if request.GET.get('sD'):
         searchquery = request.GET.get('sD')
       elif request.GET.get('sM'):
         searchquery = request.GET.get('sM')#functionality for both mobile and desktop

    articles = Article.objects.filter(title__icontains=str(searchquery)) #search string needs to be a substring of an article title
    subarticles1 = Article.objects.filter(body__icontains=str(searchquery))
    subarticles2 = Article.objects.filter(summary__icontains=str(searchquery))
    return render(request, 'articles/search.html', {"articles": articles, "articlesB": subarticles1, "articlesS": subarticles2, "query": searchquery})

def get_random(request):
    count = Article.objects.all().count()
    rand_id = random.randint(0, count-1)
    random_art = Article.objects.all()[rand_id]

    return render(request, 'articles/articleview.html', {"article": random_art, 'slug': random_art.slug})