from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home),
    path('alfabet/', views.alfabet_view, name='alfabet'),
]


