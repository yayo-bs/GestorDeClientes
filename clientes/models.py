from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_alta = models.DateField(auto_now_add=True)  # se rellena solo al crear
    activo = models.BooleanField(default=True)  # para marcar clientes de baja

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"