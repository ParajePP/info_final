from django.contrib import admin
from .models import Categoria, Publicaciones

@admin.register(Publicaciones)
class Publicaciones(admin.ModelAdmin):
    list_display=('titulo','fecha','descripcion','categoria','imagen','colaborador')




admin.site.register(Categoria)