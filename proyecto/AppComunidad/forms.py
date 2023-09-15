from django import forms
from .models import Comunidad

class crearBlogform(forms.ModelForm):
    class Meta:
        model=Comunidad
        fields=['titulo','imagen','contenido']

    imagen = forms.ImageField(label='Cargar imagen')