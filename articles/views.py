from django.shortcuts import render
from django import forms
from .forms import ArtModelForm
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your views here.
from articles.models import Article

def about(request):
    return render(request, 'articles/about.html')

def get_all_articles(request):
    articles = Article.objects.all()

    return render(request, 'articles/seeall.html', {"articles": articles, "title": "All Articles"})

def get_one_article(request, **kwargs):
    articles = Article.objects.get(pk=kwargs['pk'])

    return render(request, 'articles/articleview.html', {"article": articles})

def get_talk_page(request, **kwargs):
    talk = Talk.objects.get(pk=kwargs['pk'])

    return render(request, 'articles/talk.html', {"talk": talk})

def get_edit_page(request, **kwargs):
    articles = Article.objects.get(pk=kwargs['pk'])

    return render(request, 'articles/edit.html', {"article": articles})

def get_write_page(request):
    if request.method == "POST":
        form = ArtModelForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('frontpage')
    else:
        form = ArtModelForm()


    return render(request, "articles/write.html", {'form': form})


def get_featured_articles(request):
    articles = Article.objects.filter(featured=True)

    return render(request, 'articles/seeall.html', {"articles": articles, "title": "Featured"})

def get_front_page(request):
    articles = Article.objects.filter(featured = True)

    return render(request, 'articles/frontpage.html', {"articles": articles})