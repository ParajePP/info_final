from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario (AbstractUser):
    nombre = models.CharField(max_length=20, null=True)
    apellido= models.CharField(max_length=20, null=True)
    edad= models.CharField(max_length=2, null=True)
    is_staff= models.BooleanField( 'es_staff', default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios',default='usuarios/usuarios_def.png')
    
    def __str__(self):
        return self.nombre 
    