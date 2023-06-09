from django.urls import path
from Petstagram.common import views

ulrpatterns = [
    path('', views.index, name='index')
]