from django.urls import path
from . import views

urlpatterns = [
    # URL para el listado general de clientes
    path('', views.lista_clientes, name='lista_clientes'),
    # URL para crear un nuevo cliente
    path('nuevo/', views.crear_cliente, name='crear_cliente'),
    # URL para el detalle de un cliente específico, recibe su ID como parámetro
    path('<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    # URL para editar un cliente existente
    path('<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
]