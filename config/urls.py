from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),
    
    # Pantalla de Inicio -> Formulario de Login
    path('', auth_views.LoginView.as_view(template_name='clientes/login.html'), name='login'),
    
    # URLs de autenticación integradas (logout, cambio de contraseña, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # URLs de la app de clientes
    path('clientes/', include('clientes.urls')),
]
