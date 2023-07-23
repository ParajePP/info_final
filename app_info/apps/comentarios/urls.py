from django.urls import path
from .views import *
app_name= 'comentarios'
urlpatterns = [
    path('agregar_comentario/', AgregarComentario, name= 'agregar_comentario'),
]
