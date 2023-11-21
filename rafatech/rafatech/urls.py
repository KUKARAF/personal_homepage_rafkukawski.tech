"""rafatech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import django.contrib.auth.urls
from django.views.generic.base import TemplateView 
from . import views
urlpatterns = [
    path('robots.txt', views.robots),#meant to be used with query string 
    path('todo/', include('todo.urls')), 
    path('aglu/', include('aglu.urls')), 
    path('ap/', include('alicjas_paintings.urls')), 
    path('admin/', admin.site.urls), 
    path('accounts/',include('django.contrib.auth.urls')), 
    path('form/', TemplateView.as_view(template_name='contact.html'), name='home'), 
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('home/', TemplateView.as_view(template_name='homepage.html'), name='home'), 
]
