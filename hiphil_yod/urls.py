from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('hiphil_yod', views.hiphil_yod)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
