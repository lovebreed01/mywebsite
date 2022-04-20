from dataclasses import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=100,min_length=5,required=True)
    password1 = forms.PasswordInput() 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1' , 'password2']
