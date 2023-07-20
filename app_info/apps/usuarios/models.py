from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario (AbstractUser):
    nombre = models.CharField(max_length=20, null=True)
    apellido= models.CharField(max_length=20, null=True)
    edad= models.CharField(max_length=2, null=True)
    is_staff= models.BooleanField( default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario',default='usuario/usuario_def.png')
    
    def __str__(self):
        return self.nombre 
    