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

def get_featured_articles(request):
    articles = Article.objects.filter(featured=True)

    return render(request, 'articles/seeall.html', {"articles": articles, "title": "Featured"})