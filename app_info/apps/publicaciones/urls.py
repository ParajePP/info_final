
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

app_name= 'publicaciones'

urlpatterns = [
    path("Agregar_categoria/", AgregarCategoria.as_view(), name='Agregar_categoria'),
    path("Agregar_publicaciones/", AgregarPublicacion.as_view(), name='Agregar_publicaciones'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)