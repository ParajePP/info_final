from django.urls import path
from . import views
from .views import RegistrarUsuario

app_name = 'usuarios'
urlpatterns = [
    path("registrar/", RegistrarUsuario.as_view(), name='registrar'),
    
]
