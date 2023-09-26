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


class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Vuelve a ingresar la contraseña", widget=forms.PasswordInput)
    ingrese_nombre= forms.CharField(label="Modificar Nombre")
    ingrese_apellido= forms.CharField(label="Modificar Apellido")

    class Meta:
        model=User
        fields=['email','password1','password2','ingrese_nombre','ingrese_apellido']

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")