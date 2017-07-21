from django.contrib import admin

# Register your models here.

from create.models import create

class CreateAdmin(admin.ModelAdmin):
    pass

admin.site.register(create, CreateAdmin)