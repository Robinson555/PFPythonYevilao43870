from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):
    enviado = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
    recibido = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    contenido = models.CharField(max_length=300)
    fechaenvio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.enviado} - {self.recibido} - {self.fechaenvio}'

