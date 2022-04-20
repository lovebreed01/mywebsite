from re import template
from unicodedata import name
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]
