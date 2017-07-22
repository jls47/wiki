from django.shortcuts import render

# Create your views here.

from articles.models import Article

def about(request):
    return render(request, 'articles/about.html')

def get_all_articles(request):

    articles = Article.objects.all()

    return render(request, 'articles/article.html', {"data": articles})

def get_one_article(request, **kwargs):
    article = Article.objects.get(pk=kwargs['pk'])

    return render(request, 'articles/article.html', {"data": article})

