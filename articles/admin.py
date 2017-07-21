from django.contrib import admin

# Register your models here.

from articles.models import article

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(article, ArticleAdmin)

