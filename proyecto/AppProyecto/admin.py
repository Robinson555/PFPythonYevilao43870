from django.contrib import admin
from .models import Perros, Gatos, Fecha_Ingreso, Clientes

# Register your models here.

admin.site.register(Perros)
admin.site.register(Gatos)
admin.site.register(Fecha_Ingreso)
admin.site.register(Clientes)
