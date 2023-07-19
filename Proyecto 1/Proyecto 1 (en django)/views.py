from django.shortcuts import render 

def index (request):
    template_name= 'index.html'
    nombres = ['Noticias', 'Novedades', 'Blog', 'Perfil']
    contexto = {'nombres':nombres}
    
    return render (request, template_name, contexto)