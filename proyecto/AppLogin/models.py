from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(unique=True)
    nombre_usuario = models.CharField(max_length=40, unique=True)
    contraseña=models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.nombre}-{self.apellido}-{self.email}-{self.nombre_usuario}-{self.contraseña}"

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 