from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('sufix_posesiv_subst', views.sufix_posesiv_subst)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
