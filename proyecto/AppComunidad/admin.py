from django.contrib import admin
from .models import Comunidad, PreguntasCom, Comentario, ComentarioPregunta

# Register your models here.

admin.site.register(Comunidad)
admin.site.register(PreguntasCom)
admin.site.register(Comentario)
admin.site.register(ComentarioPregunta)