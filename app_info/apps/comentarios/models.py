from django.db import models
from apps.usuarios.models import Usuario


# Create your models here.

class Comentario(models.Model):
    contenido = models.TextField(verbose_name="comentario")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido