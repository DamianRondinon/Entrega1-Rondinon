from django.urls import path
from productos.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("inicio/", index), 
    path("/crearProducto/", views.crearProducto)
    ]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
