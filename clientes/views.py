from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Cliente
from .forms import ClienteForm

ORDEN_CAMPOS_PERMITIDOS = {
    'nombre': 'nombre',
    'apellidos': 'apellidos',
}

def lista_clientes(request):
    # Base inicial: recuperamos todos los clientes
    clientes = Cliente.objects.all()

    # 1. Obtener parámetros GET de la URL
    q = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', 'activos')

    # 2. Capturar y validar parámetros de ORDEN (?orden= Y ?dir=)
    orden = request.GET.get('orden', 'nombre').lower()
    direccion = request.GET.get('dir', 'asc').lower()

    # Validar que el campo pertenezca a la lista blanca (por defecto 'nombre')
    campo_orden = ORDEN_CAMPOS_PERMITIDOS.get(orden, 'nombre')

    # Validar dirección (por defecto 'asc')
    if direccion not in ['asc', 'desc']:
        direccion = 'asc'

    # 3. Aplicar filtro adicional (?estado=) y busqueda por texto
    if estado == 'activos':
        clientes = clientes.filter(activo=True)
    elif estado == 'inactivos':
        clientes = clientes.filter(activo=False)

    if q:
        clientes = clientes.filter(
            Q(nombre__icontains=q) | Q(apellidos__icontains=q)
        )

    # 4. Aplicar ordenamiento
    criterio_orden = (
        f'-{campo_orden}' if direccion == 'desc' else campo_orden
    )
    clientes = clientes.order_by(criterio_orden)

    context = {
        'clientes': clientes,
        'q': q,
        'estado': estado,
        'orden': orden,
        'direccion_activa': direccion,
        # Valor combinado para el <select> del template
        'orden_combina': f'{orden}_{direccion}',
    }

    # Pasamos los clientes al template mediante el contexto
    return render(request, 'clientes/lista.html', context)

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

@login_required
def eliminar_cliente(request, cliente_id):
    # Buscamos el cliente; si no existe, 404 automático
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        # Confirmación de eliminación: eliminamos el cliente
        cliente.delete()
        messages.success(request, f'Cliente "{cliente}" eliminado correctamente.')
        return redirect('lista_clientes')

    # Si es GET, mostramos la página de confirmación
    return render(request, 'clientes/confirmar_eliminacion.html', {
        'cliente': cliente,
    })
