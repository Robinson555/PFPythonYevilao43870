from django import forms

class PerrosForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    edad= forms.IntegerField()
    raza= forms.CharField(max_length=50)

class GatosForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    edad= forms.IntegerField()

class Fecha_IngresoForm(forms.Form):
    dni= forms.IntegerField()
    fecha_ingreso=forms.DateField()

class ClienteForm(forms.Form):
    dni= forms.IntegerField()
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()

