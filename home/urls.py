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
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

