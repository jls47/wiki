from django.shortcuts import render
from django import forms
from .forms import ProfModelForm
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.http import HttpResponseRedirect
import operator
from django.db.models import Q
from articles.models import Article
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from .models import Profile


def profabout(request):
    return render(request, 'profiles/about.html')

def get_all_profiles(request):

    profiles = Profile.objects.all()

    return render(request, 'profiles/all.html', {"profile": profiles})

def get_one_profile(request, name):

    profile = Profile.objects.get(name=name)

    return render(request, 'profiles/profile.html', {"profile": profile})

def write_profile(request):  # How to write an article!  This presents authenticated users with a series of forms that represent different sections of an article.
    # if this is a POST request we need to process the form data that's there and send it off.
    if request.method == "POST":
        # create a form instance and populate it with data from the request in the backend.  This is not visible to the user and happens in the blink of an eye.
        form = ProfModelForm(request.POST)
        if form.is_valid():
            # check whether it's valid.  If so, then send everything off, and set the author field to the current user's username.
            User = request.user
            model_instance = form.save()
            model_instance.name = User.username
            model_instance.timestamp = timezone.now()
            model_instance.save() #send the data to the database.  the article is created!
            print("Profile written!  Check it out!")

            return HttpResponseRedirect('/')  #back to the front page.
    else:
         # if a GET (or any other method) we'll create a blank form series for the user to populate.
        form = ProfModelForm(request.GET)
    return render(request, "profiles/write.html", {'form': form})