from django.urls import path
from .views import *

urlpatterns = [
        path('homecomunidad/', inicioComunidad, name="inicioComunidad"),
        path('aboutme/', aboutMe, name="aboutme"),
        path('contenido/', contenido, name="contenido"),
        path('crearblog/', crear_seccion, name="crearblog"),
        path('editarblog/<int:comunidad_id>/', editar_seccion, name="editar_seccion"),
        path('eliminarblog/<int:comunidad_id>/', eliminar_seccion, name="eliminar_seccion"),
        path('mensajes/<int:usuario_id>/', ver_mensajes, name='ver_mensajes'),
        path('enviar_mensaje/<int:usuario_id>/', enviar_mensaje, name='enviar_mensaje'),
        
]
