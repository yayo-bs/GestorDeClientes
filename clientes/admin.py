from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'telefono', 'activo')
    list_filter = ('activo', 'actividad')  # quita 'actividad' si no añadiste ese campo
    search_fields = ('nombre', 'apellidos', 'email')