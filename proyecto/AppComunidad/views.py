from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import crearBlogForm
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
        form = crearBlogForm(request.POST, request.FILES)
        if form.is_valid():
            seccion = form.save(commit=False)
            seccion.autor = request.user 
            seccion.save()
            return redirect('AppComunidad/homecomunidad')
    else:
        form = crearBlogForm()
    return render(request, "AppComunidad/crearblog.html", {'form': form})

@login_required
def editar_seccion(request, comunidad_id):
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    if request.method == "POST":
        form=crearBlogform(request.POST, request.FILES, instance=comunidad)
        if form.is_valid():
            form.save()
            return redirect('AppComunidad/contenido')
    else:
        form=crearBlogform(instance=comunidad)

    return render(request, "AppComunidad/editarblog.html", {'form':form, 'comunidad':comunidad})


def eliminar_seccion(request, comunidad_id):
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    if request.method == "POST":
        comunidad.delete()
        return redirect('AppComunidad/contenido')

    return render(request, "AppComunidad/eliminarblog.html", {'form':form, 'comunidad':comunidad})