"""flashcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cards/", include("cards.urls")),
    path("", views.home, name="home"),
    path("", include('home.urls')),
    path("alfabet/", include('alfabet.urls')),
    path("vowels/", include('vowels.urls')),
    path("sheva/", include('sheva.urls')),
    path("substantiv/", include('substantiv.urls')),
    path("pronume/", include('pronume.urls')),
    path("verb/", include('verb.urls')),
    path("qal_perfect", include('qal_perfect.urls')),
    path("propozitii", include('propozitii.urls')),
    path("substantiv_doi", include('substantiv_doi.urls')),
    path("prepozitii", include('prepozitii.urls')),
    path("adjectiv", include('adjectiv.urls')),
    path("qal_imperfect", include('qal_imperfect.urls')),
    path("construct_sg", include('construct_sg.urls')),
    path("construct_pl", include('construct_pl.urls')),


]
