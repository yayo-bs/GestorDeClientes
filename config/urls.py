from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),
    # URLs de la app de clieentes
    path('clientes/', include('clientes.urls')),
    # Redirige la raíz al listado de clientes
    path('', lambda request: redirect('lista_clientes')),    
]
