from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),
    # Pantalla de Inicio -> Formulario de Login
    path(
        '',
        auth_views.LoginView.as_view(template_name='clientes/login.html'),
        name='login',
    ),
    # Sobrescribimos el login de /accounts/login/ para que use tu plantilla
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='clientes/login.html'),
    ),
    # Resto de URLs de autenticación (logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # URLs de la app de clientes
    path('clientes/', include('clientes.urls')),
]
