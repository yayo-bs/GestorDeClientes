from django.shortcuts import render, get_object_or_404
from .models import Cliente

def lista_clientes(request):
    # Recuperamos solo los clientes activos de la base de datos
    clientes = Cliente.objects.filter(activo=True)  # Solo clientes activos
    # Pasamos los clientes al template mediante el contexto
    return render(request, 'clientes/lista.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    # Buscamos el cliente por ID; si no existe, devuelve error 404 automáticamente
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/detalle.html', {'cliente': cliente})
