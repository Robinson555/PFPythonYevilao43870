from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1=forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Vuelve a ingresar la contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {campo:"" for campo in fields}