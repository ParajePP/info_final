from django.shortcuts import render
from django.urls import path, include


def inicio(request):
    template_name = "inicio.html"
    return render(request, template_name)


def acerca_de(request):
    template_name = "acerca_de.html"
    return render(request, template_name)


def contacto(request):
    template_name = "contacto.html"
    return render(request, template_name)


def agregar_publicaciones(request):
    template_name = "agregar_publicaciones.html"
    return render(request, template_name)


