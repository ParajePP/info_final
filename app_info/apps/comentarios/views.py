from django.shortcuts import render

from .forms import comentarioForm

def AgregarComentario(request):
    form = comentarioForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto ={
        'form' : form,
    }
    template_name= 'comentarios/agregar_comentario.html'
    return render(request,template_name,contexto)


