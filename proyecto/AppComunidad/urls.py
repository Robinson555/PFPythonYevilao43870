from django.urls import path
from .views import *

urlpatterns = [
        #Página General del Blog
        path('homecomunidad/', inicioComunidad, name="inicioComunidad"),
        #
        #
        #Sección de "Acerca de mi"
        path('aboutme/', aboutMe, name="aboutme"),
        #
        #
        #Sección en proceso de estructuración
        path('novedades/', novedades, name="novedades"),
        #
        #
        #sección de Blog
        path('contenido/<int:comunidad_id>/', contenido, name="contenido"),
        path('contenidohome/', contenidoHome, name="contenidohome"),
        path('crearblog/', crear_seccion, name="crearblog"),
        path('editarblog/<int:comunidad_id>/', editar_seccion, name="editar_seccion"),
        path('eliminarblog/<int:comunidad_id>/', eliminar_seccion, name="eliminar_seccion"),
        #
        #
        #sección de Foro
        path('foro/<int:preguntas_id>/', foro, name="foro"),
        path('forohome/', foroHome, name="forohome"),
        path('crearforo/', crear_foro, name="crearforo"),
        path('editarforo/<int:preguntas_id>/', editar_foro, name="editarforo"),
        path('eliminarforo/<int:preguntas_id>/', eliminar_foro, name="eliminarforo"),
]

