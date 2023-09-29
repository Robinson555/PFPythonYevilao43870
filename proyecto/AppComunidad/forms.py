from django import forms
from .models import Comunidad, Mensaje

class crearBlogForm(forms.ModelForm):
    class Meta:
        model=Comunidad
        fields=['titulo','imagen','contenido','precio']

    imagen = forms.ImageField(label='Imagen de Producto', widget=forms.ClearableFileInput(attrs={'id': 'imagen'}))


class MensajeForm(forms.ModelForm):
    contenido = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Escribe tu mensaje...'}))

    class Meta:
        model = Mensaje
        fields = ['contenido']