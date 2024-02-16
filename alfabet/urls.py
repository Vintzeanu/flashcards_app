from django.urls import path

from . import views

urlpatterns = [
    path('alfabet', views.alfabet)
]
