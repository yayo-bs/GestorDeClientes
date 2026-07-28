# Práctica Módulo 5 - Gestor de Clientes

Aplicación web para la gestión integral de fichas de clientes. Permite registrar, listar, filtrar, ordenar, paginar y realizar operaciones CRUD completas con autenticación de usuarios.

## Objetivo
Construir una aplicación web sencilla que permita crear, modificar, consultar y eliminar fichas de clientes de forma intuitiva y estructurada.

## Funcionalidades previstas
- **Gestión completa (CRUD):** Crear, consultar, editar y eliminar registros de clientes.
- **Búsqueda y Filtros:** Búsqueda por texto (nombre, apellidos, email) y filtrado por estado (activos, inactivos, todos).
- **Ordenación dinámica:** Ordenar el listado por diferentes campos (`nombre`, `apellidos`, `empresa`) en sentido ascendente o descendente (`asc`/`desc`).
- **Paginación:** Navegación por páginas integrada con el mantenimiento de filtros de búsqueda.
- **Autenticación y Permisos:** Acceso mediante inicio de sesión y protección de vistas de gestión para usuarios autenticados.

## Tecnologías
- Python 3
- Django
- SQLite
- HTML5 / CSS3 / JavaScript
- Git / GitHub

---

## 🚀 Cómo ejecutar el proyecto

Sigue estos pasos para desplegar la aplicación en tu entorno local:

### 1. Clonar el repositorio e ingresar al directorio
`git clone https://github.com/yayo-bs/GestorDeClientes`
`cd M5T2_Eduardo_Bustamante_Sánchez`

### 2. Crear y activar el entorno virtual
- **En Windows (PowerShell / CMD):**
  `.venv\Scripts\activate`
- **En macOS / Linux:**
  `source .venv/bin/activate`

*(Nota: Si no has creado aún el entorno virtual, puedes crearlo previamente con `python -m venv .venv`)*

### 3. Instalar las dependencias
`pip install -r requirements.txt`
*(Si no dispones de `requirements.txt`, puedes instalar Django con `pip install django`)*.

### 4. Aplicar las migraciones
Crea la estructura de tablas en la base de datos local SQLite:
`python manage.py migrate`

### 5. Crear el superusuario (Administrador)
Genera el usuario administrador para acceder al panel de control y a todas las funciones:
`python manage.py createsuperuser`

### 6. Iniciar el servidor de desarrollo
`python manage.py runserver`

Accede a la aplicación en tu navegador web a través de: `http://127.0.0.1:8000/`

---

## 👤 Usuarios de prueba e instrucciones de acceso

Para evaluar las funciones que requieren autenticación (crear, editar y borrar registros):

* **Administrador (Superuser):**
  * **Usuario:** `admin` *(o el usuario creado en la consola)*
  * **Contraseña:** `admin123` *(o la contraseña configurada)*

### Alta de nuevos usuarios
La creación y gestión de nuevos usuarios de la plataforma se realiza exclusivamente desde el panel de administración interno de Django:
1. Accede a `http://127.0.0.1:8000/admin/` e inicia sesión con las credenciales de superusuario.
2. Navega a la sección **Usuarios** (`Authentication and Authorization > Users`).
3. Haz clic en **Añadir usuario** (`+ Add`) para dar de alta nuevas cuentas.
4. Una vez creado el usuario, este podrá iniciar sesión en la aplicación pública (`http://127.0.0.1:8000/login/`) para acceder a las funciones avanzadas de gestión de clientes.

---

## 🔗 Ejemplos de URLs con parámetros

El listado principal de clientes permite combinar parámetros GET de búsqueda (`q`), filtro de estado (`estado`), campo de ordenación (`order`), dirección (`dir`) y página (`page`):

* **Búsqueda por texto y ordenación ascendente por nombre:**
  `http://127.0.0.1:8000/clientes/?q=eduardo&order=nombre&dir=asc`

* **Filtrado de clientes activos ordenados descendentemente por apellidos:**
  `http://127.0.0.1:8000/clientes/?estado=activos&order=apellidos&dir=desc`

* **Búsqueda general con filtro de inactivos en la página 2:**
  `http://127.0.0.1:8000/clientes/?q=sanchez&estado=inactivos&page=2`

* **Consulta combinada completa (Búsqueda + Estado + Ordenación + Paginación):**
  `http://127.0.0.1:8000/clientes/?q=garcia&estado=todos&order=apellidos&dir=asc&page=2`

---

## Autor
- Eduardo Bustamante Sánchez

## Fecha de creación
06/2026