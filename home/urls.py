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
    path("construct_sg/", views.construct_sg_view, name="construct_sg"),
    path("construct_pl/", views.construct_pl_view, name="construct_pl"),
    path("qal_radacini_slabe/", views.qal_radacini_slabe_view, name="qal_radacini_slabe"),
    path("sufix_posesiv_subst/", views.sufix_posesiv_subst_view, name="sufix_posesiv_subst"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

