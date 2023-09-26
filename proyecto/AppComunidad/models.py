from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comunidad(models.Model):
    titulo= models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField()
    fecha_creacion=models.DateField(auto_now=True)
    precio = models.CharField(max_length=8)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.autor} - { self.titulo}"


class PreguntasCom(models.Model):
    titulo= models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField()
    fecha_creacion=models.DateField(auto_now=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.autor} - { self.titulo}"


