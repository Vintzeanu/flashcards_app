from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('este_si_are', views.este_si_are)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
