from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.


class AgregarCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'publicaciones/agregar_categoria.html'
    success_url = reverse_lazy('inicio')
    
class AgregarPublicaciones(CreateView):
    model = Publicaciones
    fields = ['titulo','empresa','descripcion','is_staff','categoria']
    template_name = 'publicaciones/agregar_publicaciones.html'
    success_url = reverse_lazy('inicio')