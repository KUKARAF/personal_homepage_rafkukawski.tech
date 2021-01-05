from django.urls import path

from . import views
from .views import create_painting
urlpatterns = [
    path('', views.template_index, name='template_index'),
    path('create', views.create_painting),
    path('painting/<int:painting_id>', views.template_painting),
]
