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
    path("qal_radacini_slabe", include('qal_radacini_slabe.urls')),
    path("sufix_posesiv_subst", include('sufix_posesiv_subst.urls')),
    path("demonstrativ_relativ", include('demonstrativ_relativ.urls')),
    path("sufix_posesiv_pl", include('sufix_posesiv_pl.urls')),
    path("qal_infinitiv", include('qal_infinitiv.urls')),
    path("qal_activ", include('qal_activ.urls')),
    path("sufix_pronominal", include('sufix_pronominal.urls')),
    path("este_si_are", include('este_si_are.urls')),
    path("qal_volitiv", include('qal_volitiv.urls')),
    path("qal_verbe_slabe", include('qal_verbe_slabe.urls')),
    path("relativ_waw", include('relativ_waw.urls')),
    path("temporal_interogativ", include('temporal_interogativ.urls')),
    path("piel_radacini_tari", include('piel_radacini_tari.urls')),
    path("piel_radacini_slabe", include('piel_radacini_slabe.urls')),
    path("surpriza", include('surpriza.urls')),
    path("numeralul", include('numeralul.urls')),
    path("hiphil_radacini_tari", include('hiphil_radacini_tari.urls')),
    path("hiphil_gutural_nun", include('hiphil_gutural_nun.urls')),
    path("hiphil_yod", include('hiphil_yod.urls')),
    path("hiphil_he_gaunoase", include('hiphil_he_gaunoase.urls')),
    path("pronume_mai_mult", include('pronume_mai_mult.urls')),
    path("niphal_radacini_tari", include('niphal_radacini_tari.urls')),
    path("niphal_radacini_slabe", include('niphal_radacini_slabe.urls')),
    path("verbe_pasive", include('verbe_pasive.urls')),
    path("hithpael", include('hithpael.urls')),
]
