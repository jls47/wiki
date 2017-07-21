from django.contrib import admin

# Register your models here.

from login.models import login

class LoginAdmin(admin.ModelAdmin):
    pass

admin.site.register(login, LoginAdmin)