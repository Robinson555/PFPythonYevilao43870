from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Vuelve a ingresar Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {campo:"" for campo in fields}

    imagen = forms.ImageField(label="Imagen de Perfil", required=False)


class UserEditForm(UserCreationForm):
    nombre = forms.CharField(label="Modificar Nombre")
    apellido = forms.CharField(label="Modificar Apellido")
    email = forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Vuelve a ingresar la contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['nombre','apellido','email','password1','password2']

    imagen = forms.ImageField(label="Imagen de Perfil", required=False)

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
