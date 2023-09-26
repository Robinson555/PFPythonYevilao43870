from django.urls import path
from .views import *

urlpatterns = [
        path('homecomunidad/', inicioComunidad, name="inicioComunidad"),
        path('abaoutme/', abaoutMe, name="abaoutme"),
        path('contenido/', contenido, name="contenido"),
        path('crearblog/', crear_seccion, name="crearblog"),
        path('editarblog/', editar_seccion, name="editar_seccion"),
        path('eliminarblog/', eliminar_seccion, name="eliminar_seccion"),
]
