from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import crearBlogform
from .models import Comunidad

# Create your views here.

def inicioComunidad(request):
    return render(request, "AppComunidad/homecomunidad.html")

def abaoutMe(request):
    return render(request, "AppComunidad/abaoutme.html")

def contenido(request):
    return render(request, "AppComunidad/contenido.html")

@login_required
def crear_seccion(request):
    if request.method == "POST":
        form=crearBlogform(request.POST, request.FILES)
        if form.is_valid():
            seccion=form.save(commit=False)
            seccion.creador=request.User
            seccion.save()
            return redirect('inicioComunidad')

    else:
        form=crearBlogform()
    return render(request, "crearblog.html", {'form':form})

@login_required
def editar_seccion(request, comunidad_id):
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    if request.method == "POST":
        form=crearBlogform(request.POST, request.FILES, instance=comunidad)
        if form.is_valid():
            form.save()
            return redirect('contenido')
    else:
        form=crearBlogform(instance=comunidad)

    return render(request, "editarblog.html", {'form':form, 'comunidad':comunidad})

@login_required
def eliminar_seccion(request, comunidad_id):
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    if request.method == "POST":
        comunidad.delete()
        return redirect('contenido')

    return render(request, "eliminarblog.html", {'form':form, 'comunidad':comunidad})