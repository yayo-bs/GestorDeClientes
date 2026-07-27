from django.db import models

class Cliente(models.Model):

    # Definimos una lista de tuplas con opciones predefinidas para las actividades.
    ACTIVIDADES = [
        ('danza', 'Danza'),
        ('yoga', 'Yoga'),
        ('pilates', 'Pilates'),
        ('funcional', 'Entrenamiento funcional'),
    ]
    
    # Datos de identificación del cliente
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)

    # Datos de contacto
    email = models.EmailField(unique=True)  # unique evita emails duplicados
    telefono = models.CharField(max_length=15)

    # Datos de gestión interna
    fecha_alta = models.DateField(auto_now_add=True)  # se rellena automáticamente al crear
    activo = models.BooleanField(default=True)  # permite dar de baja sin borrar el registro
    actividad = models.CharField(max_length=20, choices=ACTIVIDADES, default='danza')

    # null=True y blank=True porque los clientes ya existentes en la base de datos
    # no tienen este dato, y no queremos obligar a rellenarlo siempre.
    proxima_cita = models.DateField(null=True, blank=True)

    def __str__(self):
        # Representación legible del objeto en el admin
        return f"{self.nombre} {self.apellidos}"