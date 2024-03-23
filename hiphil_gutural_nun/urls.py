from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('hiphil_gutural_nun', views.hiphil_gutural_nun)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
