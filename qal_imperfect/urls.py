from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from . import views

urlpatterns = [
    path('qal_imperfect', views.qal_imperfect),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
