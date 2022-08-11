from django.urls import path
from productos.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("inicio/", index), 
    path("producto/crear/", crear_producto, name="producto_crear")
    ]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
