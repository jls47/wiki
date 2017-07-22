from django.contrib import admin

# Register your models here.

from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)

