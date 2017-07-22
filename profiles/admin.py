from django.contrib import admin

# Register your models here.

from profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)