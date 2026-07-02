from django.db import models

class Cliente(models.Model):

    # Definimos una lista de tuplas para las actividades disponibles. Cada tupla contiene un valor interno y un valor legible para el usuario.
    ACTIVIDADES = [
        ('danza', 'Danza'),
        ('yoga', 'Yoga'),
        ('pilates', 'Pilates'),
        ('funcional', 'Entrenamiento funcional'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_alta = models.DateField(auto_now_add=True)  # se rellena solo al crear
    activo = models.BooleanField(default=True)  # para marcar clientes de baja
    actividad = models.CharField(max_length=20, choices=ACTIVIDADES, default='danza')

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"