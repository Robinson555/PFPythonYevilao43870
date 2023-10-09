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

        

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='media/avatars/', blank=True, null=True)
    respuesta_a = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')

    def __str__(self):
        return f'Comentario por {self.autor} en {self.publicacion.titulo}'

    def get_absolute_url(self):
        return reverse('detalle_publicacion', args=[str(self.publicacion.id)])

class ComentarioPregunta(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(PreguntasCom, on_delete=models.CASCADE)
    contenidop = models.TextField(blank=True) 
    fecha = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='media/avatars/', blank=True, null=True)
    respuesta_b = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario por {self.autor} en {self.publicacion.titulo}'

    def get_absolute_url(self):
        return reverse('detalle_publicacion', args=[str(self.publicacion.id)])

