from django.shortcuts import render 
from django.urls import path, icnlude
from .views import inicio

def index (request):
    template_name= 'index.html'
    nombres = ['Noticias', 'Novedades', 'Blog', 'Perfil']
    contexto = {'nombres':nombres}
    
    return render (request, template_name, contexto)

def inicio (request):
    template_name='inicio.html'
    return render (request, template_name)