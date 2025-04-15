# File: hello_world_app/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')

# File: hello_world_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello_world_app.urls')),
]

# File: hello_world_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
]

def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')