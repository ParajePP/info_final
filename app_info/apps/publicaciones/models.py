from typing import Any, Dict, Tuple
from django.db import models
from django.utils import timezone
# Create your models here.
from apps.usuarios.models import Usuario




#categoría
class Categoria(models.Model):
    nombre=models.CharField(max_length=30, null=False, default='Valor Predeterminado')

    def str(self):
        return self.nombre

class Publicaciones(models.Model):
    titulo=models.CharField(max_length=50, null=False)
    empresa=models.CharField(max_length=100, null=True, blank=True)
    fecha=models.DateTimeField(auto_now_add=True)
    descripcion=models.TextField(null=False)
    activo=models.BooleanField(default=True)
    colaborador = models.ForeignKey(Usuario, on_delete= models.SET_NULL, null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default= 1)
    imagen=models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.jpg')
    publicado=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=('-publicado'),


    def str(self) -> str:
        return self.titulo

    def delete(self, using=None , keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()
