from django.urls import path
from .views import *

urlpatterns = [
        path('perros/', crear_perro, name="perros"),
        path('gatos/', crear_gato, name="gatos"),
        path('fechaIngreso/', fecha_ingreso , name="fechaIngreso"),
        path('clientes/', clientes, name="clientes"),
        path('busquedaCliente/', busquedaCliente, name="busquedaCliente"),
        path('resultadobusqueda/', resultadobusqueda, name="resultadobusqueda"),
]
