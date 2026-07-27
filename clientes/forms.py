from datetime import date
from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    """
    Formulario para crear y editar clientes.
    Se usa el mismo formulario para ambas vistas (crear_cliente y editar_cliente).
    """

    class Meta:
        model = Cliente
        # No incluimos 'fecha_alta' porque es auto_now_add=True:
        # Django la rellena solo al crear y no debe ser editable por el usuario.
        fields = ['nombre', 'apellidos', 'email', 'telefono', 'activo', 'actividad', 'proxima_cita']

        # Mensajes de error personalizados para los campos obligatorios.
        error_messages = {
            'nombre': {'required': 'El nombre es obligatorio.'},
            'apellidos': {'required': 'Los apellidos son obligatorios.'},
            'email': {'required': 'El email es obligatorio.'},
            'telefono': {'required': 'El teléfono es obligatorio.'},
        }

        # widgets: personalizamos cómo se renderiza cada campo en el HTML.
        # Sin esto, Django mostraría 'proxima_cita' como un simple <input type="text">.
        # type='date' hace que el navegador muestre un selector de calendario nativo.
        widgets = {
            'proxima_cita': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_telefono(self):
        """
        Validación personalizada del campo teléfono.
        Django ejecuta automáticamente cualquier método clean_<nombre_campo>
        antes de guardar el formulario.
        """
        telefono = self.cleaned_data.get('telefono')

        if telefono is None:
            raise forms.ValidationError('El teléfono es obligatorio.')

        telefono = telefono.strip()

        if not telefono:
            raise forms.ValidationError('El teléfono es obligatorio.')

        # Comprobamos que el teléfono contenga solo dígitos (sin +, espacios, guiones, etc.)
        if not telefono.isdigit():
            raise forms.ValidationError('El teléfono debe contener solo números.')

        # Comprobamos una longitud mínima razonable
        if len(telefono) < 9:
            raise forms.ValidationError('El teléfono debe tener al menos 9 dígitos.')

        return telefono

    def clean_proxima_cita(self):
        """
        Validación personalizada: la próxima cita no puede ser una fecha pasada.
        Como el campo es opcional (blank=True), solo validamos si el usuario
        introdujo un valor.
        """
        proxima_cita = self.cleaned_data.get('proxima_cita')

        if proxima_cita and proxima_cita < date.today():
            raise forms.ValidationError('La fecha de la próxima cita no puede ser anterior a hoy.')

        return proxima_cita