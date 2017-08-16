from django.shortcuts import render
from django import forms
from .forms import ArtModelForm
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.http import HttpResponseRedirect
import operator
from django.db.models import Q
from articles.models import Article
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView


def about(request):
    return render(request, 'articles/about.html')

def get_all_articles(request):
    articles = Article.objects.all()

    return render(request, 'articles/seeall.html', {"articles": articles, "title": "All Articles"})

def get_one_article(request, slug):
    articles = Article.objects.get(slug=slug)


    return render(request, 'articles/articleview.html', {"article": articles})

def get_talk_page(request, slug):
    talk = Talk.objects.get(slug=slug)

    return render(request, 'articles/talk.html', {"talk": talk})

def get_edit_page(request, slug):
        if request.method == POST and 'Post' in request.POST:
            form = ArtModelForm(slug, request.POST)
            if form.is_valid():
                model_instance = form.save()
                model_instance.timestamp = timezone.now()
                model_instance.save()
                return redirect('/')
        else:
            #attempting to create a populated form
            article = Article.objects.get(slug=slug)
            form = ArtModelForm(initial={'title': article.title, 'summary': article.summary, 'body': article.body, 'category': article.category})
            return render(request, "articles/edit.html", {'form': form})


def get_write_page(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST" and 'Post' in request.POST:
        # create a form instance and populate it with data from the request:
        form = ArtModelForm(request.POST)
        if form.is_valid():
            # check whether it's valid:
            model_instance = form.save()
            model_instance.timestamp = timezone.now()
            model_instance.save()
            print("Page written!  Check it out!")

            return redirect('/')
    else:
         # if a GET (or any other method) we'll create a blank form
        form = ArtModelForm(request.GET)


    return render(request, "articles/write.html", {'form': form})

def get_categories(request):
    paginate_by = 10


    if request.method == "GET":
        cat = request.GET.get('categ')
    articles = Article.objects.filter(category_icontains=cat)

    return render(request, 'articles/categories.html', {"articles": articles, "category": cat})



def get_featured_articles(request):
    articles = Article.objects.filter(featured=True)

    return render(request, 'articles/seeall.html', {"articles": articles, "title": "Featured"})

def get_front_page(request):
    articles = Article.objects.filter(featured = True)

    return render(request, 'articles/frontpage.html', {"articles": articles})

def get_search(request):
    paginate_by = 10


    if request.method == "GET":
       if request.GET.get('sD'):
         searchquery = request.GET.get('sD')
       elif request.GET.get('sM'):
         searchquery = request.GET.get('sM')

    articles = Article.objects.filter(title__icontains=str(searchquery)) #Having trouble getting the actual search text in here

    return render(request, 'articles/search.html', {"articles": articles, "query": searchquery})