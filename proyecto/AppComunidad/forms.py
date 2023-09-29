from django import forms
from .models import Comunidad

class crearBlogForm(forms.ModelForm):
    class Meta:
        model=Comunidad
        fields=['titulo','imagen','contenido','precio']

    imagen = forms.ImageField(label='Cargar imagen')