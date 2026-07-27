from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm


@login_required
def lista_clientes(request):
    # Recuperamos solo los clientes activos de la base de datos
    clientes = Cliente.objects.filter(activo=True)  # Solo clientes activos
    # Pasamos los clientes al template mediante el contexto
    return render(request, 'clientes/lista.html', {'clientes': clientes})

@login_required
def detalle_cliente(request, cliente_id):
    # Buscamos el cliente por ID; si no existe, devuelve error 404 automáticamente
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/detalle.html', {'cliente': cliente})

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        # Si se envió el formulario, lo construimos con los datos recibidos
        form = ClienteForm(request.POST)
        if form.is_valid():
            # form.save() crea el objeto Cliente en la base de datos
            # y nos devuelve la instancia ya guardada (con su id asignado)
            cliente = form.save()
            messages.success(request, f'Cliente "{cliente}" creado correctamente.')
            return redirect('detalle_cliente', cliente_id=cliente.id)
        # Si no es válido, no hacemos nada especial aquí:
        # el form con errores se vuelve a renderizar más abajo, con los mensajes
        # de clean_telefono / clean_proxima_cita / campos obligatorios ya incluidos.
    else:
        # Petición GET: mostramos el formulario vacío
        form = ClienteForm()

    return render(request, 'clientes/form_cliente.html', {
        'form': form,
        'titulo': 'Nuevo cliente',
    })


@login_required
def editar_cliente(request, cliente_id):
    # Buscamos el cliente existente; si no existe, 404 automático
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        # instance=cliente es la clave para EDITAR en vez de crear:
        # le decimos a Django "actualiza este objeto concreto", no crees uno nuevo
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f'Cliente "{cliente}" actualizado correctamente.')
            return redirect('detalle_cliente', cliente_id=cliente.id)
    else:
        # Petición GET: mostramos el formulario precargado con los datos actuales
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/form_cliente.html', {
        'form': form,
        'cliente': cliente,
        'titulo': f'Editar cliente: {cliente}',
    })
