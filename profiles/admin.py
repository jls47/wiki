from django.contrib import admin

# Register your models here.

from profiles.models import profile

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(profile, ProfileAdmin)