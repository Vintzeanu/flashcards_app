from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('niphal_radacini_slabe', views.niphal_radacini_slabe)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
