# mi_aplicacion/forms.py

from django import forms
from .models import Publicaciones, Comentarios

class PublicacionesForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['titulo', 'empresa', 'descripcion', 'categoria', 'published']
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model= Comentarios 
        fields = ['mensaje']
