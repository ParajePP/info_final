from django.shortcuts import render 
from django.urls import path, include

#def index (request):
    #template_name= 'inicio.html'
    #nombres = ['Noticias', 'Novedades', 'Blog', 'Perfil']
    #contexto = {'nombres':nombres}
    
    #return render (request, template_name, contexto)

def inicio (request):
    template_name='inicio.html'
    return render (request, template_name)

def acerca_de (request):
    template_name='acerca_de.html'
    return render (request, template_name)

def contacto (request):
    template_name='contacto.html'
    return render (request, template_name)