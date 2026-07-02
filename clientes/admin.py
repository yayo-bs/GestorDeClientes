from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'telefono', 'activo', 'actividad')
    list_filter = ('activo', 'actividad')
    search_fields = ('nombre', 'apellidos', 'email')