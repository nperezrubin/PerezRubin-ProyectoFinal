from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Imagen

def validate_password(password):
    if not any(char.isdigit() for char in password): #validamos que la pass al menos incluya un número
        raise ValidationError("The password must contain at least one number.")

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, validators=[validate_password])
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}


class UserEditForm(UserChangeForm): # Hereda de UserChangeForm, que es un formulario de Django predefinido para modificar usuarios existentes
    password = None  # Desactiva el campo de contraseña en este formulario, evitando que los usuarios cambien su contraseña a través de él.

    # Define los campos del formulario con sus respectivas etiquetas
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')            
    imagen = forms.ImageField(label="Avatar", required=False)  # Campo para subir una imagen de avatar. No es obligatorio (required=False)

    class Meta: # Esta clase interna proporciona metadatos sobre el formulario
        model = User     # Indica que este formulario está asociado al modelo de usuario de Django
        fields = ['email', 'last_name', 'first_name', 'imagen']  # Lista los campos que se incluirán en el formulario (en el orden en que se mostrarán)





