from django.contrib import admin

# Register your models here.

from create.models import Create

class CreateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Create, CreateAdmin)