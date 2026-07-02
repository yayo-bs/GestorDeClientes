from django.urls import path
from . import views

urlpatterns = [
    # URL para el listado general de clientes
    path('', views.lista_clientes, name='lista_clientes'),
    # URL para el detalle de un cliente específico, recibe su ID como parámetro
    path('<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
]