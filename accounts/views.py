
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from accounts.forms import RegistrationForm
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

