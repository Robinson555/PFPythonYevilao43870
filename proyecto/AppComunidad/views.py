from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppLogin.forms import RegistroUsuarioForm, UserEditForm, AvatarForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import crearBlogForm
from .models import Comunidad

# Create your views here.
@login_required
def inicioComunidad(request):
    return render(request, "AppComunidad/homecomunidad.html")

@login_required
def aboutMe(request):
    return render(request, "AppComunidad/aboutme.html")

@login_required
def contenido(request):
    publicaciones = Comunidad.objects.all()
    return render(request, "AppComunidad/contenido.html", {'publicaciones': publicaciones})

#Función para crear publicaciones
@login_required
def crear_seccion(request):
    if request.method == "POST":
        form = crearBlogForm(request.POST, request.FILES)
        if form.is_valid():
            seccion = form.save(commit=False)
            seccion.autor = request.user 
            seccion.save()
            return redirect('inicioComunidad')
    else:
        form = crearBlogForm()
    return render(request, "AppComunidad/crearblog.html", {'form': form})


#Función para editar publicaciones
@login_required
def editar_seccion(request, comunidad_id):
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    if comunidad.autor == request.user:
        if request.method == "POST":
            form = crearBlogForm(request.POST, request.FILES, instance=comunidad)
            if form.is_valid():
                form.save()
                return redirect('contenido')
        else:
            form = crearBlogForm(instance=comunidad)
        
        return render(request, "AppComunidad/editarblog.html", {'form': form, 'comunidad': comunidad})
    else:
        return HttpResponseForbidden("No tienes permisos para editar esta publicación")


#Función para eliminar publicaciones
@login_required
def eliminar_seccion(request, comunidad_id):
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    if comunidad.autor == request.user:
        if request.method == "POST" or 'eliminar' in request.POST:
            comunidad.delete()
            return redirect('contenido')
        else:
            return render(request, "AppComunidad/eliminarblog.html", {'comunidad': comunidad})
    else:
        return HttpResponseForbidden("No tienes permisos para eliminar esta publicación")


        