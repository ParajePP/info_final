from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *



# Create your views here.
class AgregarCategoria(CreateView):
    model = Categoria
    fields=['nombre']
    template_name= 'publicaciones/Agregar_categoria.html'
    success_url= reverse_lazy('inicio')
    
class AgregarPublicacion(CreateView):
    model = Categoria
    fields=['titulo', 'empresa', 'descripcion', 'fecha', 'imagen','categoria']
    template_name= 'publicaciones/Agregar_publicaciones.html'
    success_url= reverse_lazy('inicio')
    
    