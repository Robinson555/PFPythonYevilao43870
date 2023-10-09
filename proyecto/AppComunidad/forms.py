from django import forms
from .models import Comunidad, PreguntasCom, Comentario, ComentarioPregunta

class crearBlogForm(forms.ModelForm):
    class Meta:
        model=Comunidad
        fields=['titulo','imagen','contenido','precio']

    imagen = forms.ImageField(label='Imagen de Producto', widget=forms.ClearableFileInput(attrs={'id': 'imagen'}))

class crearForoForm(forms.ModelForm):
    class Meta:
        model = PreguntasCom
        fields = ['titulo', 'imagen', 'contenido']

    imagen = forms.ImageField(label='Imagen', widget=forms.ClearableFileInput(attrs={'id': 'imagen'}))


class comentarioForm(forms.ModelForm):
    respuesta_a = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model  = Comentario
        fields = ['contenido']

class comentarioPregunta(forms.ModelForm):
    respuesta_b = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = ComentarioPregunta 
        fields = ['contenidop']