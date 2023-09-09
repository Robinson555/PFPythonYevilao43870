from django.shortcuts import render
from .models import Gatos, Perros, Fecha_Ingreso, Clientes
from django.http import HttpResponse
from .forms import PerrosForm, GatosForm, Fecha_IngresoForm, ClienteForm

# Create your views here.

#Inicio de Pagina
def inicio(request):
    return render(request, "AppProyecto/inicio.html")

#SECCION DE BUSQUEDA DE CLIENTE VETERINARIA

def busquedaCliente(request):
    return render(request, "AppProyecto/busquedaCliente.html")

def resultadobusqueda(request): #se va a encargar de buscar los datos, va con el de arriba
    dni=request.GET["dni"]
    if dni!="":
        dni=Clientes.objects.filter(dni__icontains=dni) #icontains(Contiene un digito y busca similitudes)
        return render(request,"AppProyecto/resultadosCliente.html", {"clientes":dni})
    else:
        return render(request,"AppProyecto/busquedaCliente.html", {"mensaje":"No hay valores ingresados"})


#SECCION VIEWS PERROS

def crear_perro(request):
    if request.method=="POST":
        form=PerrosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            edad=info["edad"]
            raza=info["raza"]
            nuevo_perro=Perros(nombre=nombre,edad=edad,raza=raza)
            nuevo_perro.save()
            formulario_perros=PerrosForm()
            return render(request,"AppProyecto/perros.html", {"mensaje":"Paciente Creado", "formulario":formulario_perros})
        else:
            return render(request,"AppProyecto/perros.html", {"mensaje":"Datos no validos"}) 
    else:
        formulario_perros=PerrosForm()

    return render(request,"AppProyecto/perros.html", {"formulario":formulario_perros})


#SECCION VIEWS GATOS

def crear_gato(request):
    if request.method=="POST":
        form=GatosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            edad=info["edad"]
            nuevo_gato=Gatos(nombre=nombre,edad=edad)
            nuevo_gato.save()
            formulario_gatos=GatosForm()
            return render(request,"AppProyecto/gatos.html", {"mensaje":"Paciente Creado", "formulario":formulario_gatos})
        else:
            return render(request,"AppProyecto/gatos.html", {"mensaje":"Datos no validos"}) 
    else:
        formulario_gatos=GatosForm()

    return render(request,"AppProyecto/gatos.html", {"formulario":formulario_gatos})


#SECCION VIEWS PERROS

def fecha_ingreso(request):
    if request.method=="POST":
        form=Fecha_IngresoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            dni=info["dni"]
            fecha_ingreso=info["fecha_ingreso"]
            nuevo_ingreso=Fecha_Ingreso(dni=dni,fecha_ingreso=fecha_ingreso)
            nuevo_ingreso.save()
            formulario_fecha_ingreso=Fecha_IngresoForm()
            return render(request,"AppProyecto/fechaIngreso.html", {"mensaje":"Cliente Ingresado a la Plataforma", "formulario":formulario_fecha_ingreso})
        else:
            return render(request,"AppProyecto/fechaIngreso.html", {"mensaje":"Datos no validos"}) 
    else:
        formulario_fecha_ingreso=Fecha_IngresoForm()

    return render(request,"AppProyecto/fechaIngreso.html", {"formulario":formulario_fecha_ingreso})


#SECCION VIEWS CLIENTES

def clientes(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            dni=info["dni"]
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            nuevo_cliente=Clientes(dni=dni,nombre=nombre,apellido=apellido,email=email)
            nuevo_cliente.save()
            formulario_cliente=ClienteForm()
            return render(request,"AppProyecto/clientes.html", {"mensaje":"Cliente Creado", "formulario":formulario_cliente})
        else:
            return render(request,"AppProyecto/clientes.html", {"mensaje":"Datos no validos"}) 
    else:
        formulario_cliente=ClienteForm()

    return render(request,"AppProyecto/clientes.html", {"formulario":formulario_cliente})
