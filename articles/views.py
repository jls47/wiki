from django.shortcuts import render

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

def get_create_page(request):

    return render(request, 'articles/create.html')

def get_featured_articles(request):
    articles = Article.objects.filter(featured=True)

    return render(request, 'articles/seeall.html', {"articles": articles, "title": "Featured"})

def get_front_page(request):
    articles = Article.objects.filter(featured = True)

    return render(request, 'articles/frontpage.html', {"articles": articles})