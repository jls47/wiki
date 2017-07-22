from django.contrib import admin

# Register your models here.

from login.models import Login

class LoginAdmin(admin.ModelAdmin):
    pass

admin.site.register(Login, LoginAdmin)