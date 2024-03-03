from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('home', views.home),
    path('alfabet/', views.alfabet_view, name='alfabet'),
    path('vowels/', views.vowels_view, name='vowels'),
    path('sheva/', views.sheva_view, name='sheva'),
    path("substantiv/", views.substantiv_view, name='substantiv'),
    path("pronume/", views.pronume_view, name='pronume'),
    path("verb/", views.verb_view, name='verb'),
    path("qal_perfect/", views.qal_perfect_view, name="qal_perfect"),
    path("propozitii/", views.propozitii_view, name="propozitii"),
    path("substantiv_doi/", views.substantiv_doi_view, name="substantiv_doi"),
    path("prepozitii/", views.prepozitii_view, name="prepozitii"),
    path("adjectiv/", views.adjectiv_view, name="adjectiv"),
    path("qal_imperfect/", views.qal_imperfect_view, name="qal_imperfect"),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

