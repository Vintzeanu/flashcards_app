from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('pronume_mai_mult', views.pronume_mai_mult)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
