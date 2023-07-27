
import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from app_info.views import inicio
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    
urlpatterns = [
   path("registrar/",RegistrarUsuario.as_view(), name='registrar.html'),
   path('iniciar_sesion/', LoginView.as_view(template_name = 'usuarios/iniciar_sesion.html'), name='iniciar_sesion'),
   path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
   path('listar_usuarios/', ListarUsuarios, name='listar_usuarios'),
   ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += statistics(settings.STATIC_URL, document_root=settings.STATIC_ROOT)