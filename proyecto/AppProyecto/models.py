from django.db import models

# Create your models here.

class Perros(models.Model):
    nombre= models.CharField(max_length=50)
    edad=models.IntegerField()
    raza=models.CharField(max_length=20) #la raza se consulta para saber si es paciente de riesgo.
    def __str__(self):
        return f"{self.nombre} - {self.edad}"

class Gatos(models.Model):
    nombre= models.CharField(max_length=50)
    edad=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.edad}"

class Fecha_Ingreso(models.Model):
    dni=models.IntegerField()
    fecha_ingreso=models.DateField()
    def __str__(self):
        return f"{self.dni} - {self.fecha_ingreso}"

class Clientes(models.Model):
    dni=models.IntegerField()
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    def __str__(self):
        return f"{self.dni} - {self.apellido}"

