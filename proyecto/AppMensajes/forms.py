from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Mensaje

class formularioMensaje(forms.Form):
    envio = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))
    recibido = forms.ModelChoiceField(label="Para", queryset=User.objects.all())

