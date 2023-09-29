from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comunidad(models.Model):
    titulo= models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField()
    fecha_creacion=models.DateField(auto_now=True)
    precio = models.CharField(max_length=10)
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

#mensajeria

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'De {self.emisor.username} a {self.receptor.username}'

    class Meta:
        ordering = ['fecha_envio']