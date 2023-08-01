from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, BaseDeleteView
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.


class AgregarCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'publicaciones/agregar_categoria.html'
    success_url = reverse_lazy('inicio')
    

@login_required
def agregar_publicaciones(request):
    if request.method == 'POST':
        form = PublicacionesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio') 
    else : 
        form=PublicacionesForm() 
        
    return render(request, 'publicaciones/agregar_publicaciones.html', {'form': form})

class VerPublicaciones(ListView):
    model= Publicaciones
    template_name= 'publicaciones/ver_publicaciones.html'
    context_object_name= 'publicaciones'
    ordering= ['-id']
    
    
class DetallePublicacion(DetailView):
    model= Publicaciones
    template_name= 'publicaciones/detalle_publicacion.html'
    context_object_name= 'publicacion'
    
    def get_context_data(self,**kwargs):
        publicacion= self.get_object()
        comentarios= publicacion.comentarios.all()
        context=super().get_context_data(**kwargs)
        context['comentarios']=comentarios
        context['comentario_form']=ComentarioForm()
        return context
    
@login_required

def agregar_comentario(request, pk):
    publicacion = get_object_or_404(Publicaciones, pk=pk)
    if request.method == "POST": 
        form = ComentarioForm(request.POST)
        if form.is_valid():
            
            comentario = form.save(commit=False)
            comentario.autor = request.user 
            comentario.publicacion = publicacion  # establecemos el campo para las publicaciones
            comentario.save()
            return redirect(reverse('apps.publicaciones:detalle', kwargs={'pk': pk}))
    else:
        form = ComentarioForm()

    return render(request, 'publicaciones/comentario/agregar_comentario.html', {'publicacion': publicacion, "formulario_comentario": form})
