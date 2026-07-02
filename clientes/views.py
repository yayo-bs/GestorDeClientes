from django.shortcuts import render, get_object_or_404
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.filter(activo=True)  # Solo clientes activos
    return render(request, 'clientes/lista.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/detalle.html', {'cliente': cliente})
