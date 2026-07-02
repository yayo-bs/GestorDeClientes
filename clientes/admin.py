from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Columnas visibles en el listado de admin
    list_display = ('nombre', 'apellidos', 'email', 'telefono', 'activo', 'actividad')
    # Filtros en la barra lateral derecha
    list_filter = ('activo', 'actividad')
    # Campos por los que se puede buscar en el admin
    search_fields = ('nombre', 'apellidos', 'email')