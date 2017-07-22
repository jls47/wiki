from django.shortcuts import render

# Create your views here.
from profiles.models import Profile

def about(request):
    return render(request, 'profiles/about.html')

def get_all_profiles(request):

    profiles = Profile.objects.all()

    return render(request, 'profiles/profile.html', {"data": profiles})

def get_one_profile(request, **kwargs):
    profile = Profile.objects.get(pk=kwargs['pk'])

    return render(request, 'profiles/profile.html', {"data": profile})

