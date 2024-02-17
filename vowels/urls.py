from django.urls import path

from . import views

urlpatterns = [
    path('vowels', views.vowels)
]
