from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def signup(request):  
    if request.method == 'POST':
        user = User.objects.create_user(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password1']
            )
        login(request, user)
        return redirect('home')
    return render(request, 'user/signup.html')

