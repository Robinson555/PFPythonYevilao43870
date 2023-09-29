from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppLogin.forms import RegistroUsuarioForm, UserEditForm, AvatarForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AppLogin.views import *
from AppLogin.models import*
from .forms import crearBlogForm, MensajeForm
from .models import Comunidad

# Create your views here.

def inicioComunidad(request):
    avatar= obtenerAvatar(request)
    
    return render(request,"AppComunidad/homecomunidad.html", {"avatar":obtenerAvatar(request)})

@login_required
def aboutMe(request):
    avatar= obtenerAvatar(request)
    return render(request, "AppComunidad/aboutme.html", {"avatar":obtenerAvatar(request)})

@login_required
def contenido(request):
    publicaciones = Comunidad.objects.all()

    avatar=obtenerAvatar(request)
    return render(request, "AppComunidad/contenido.html", {'publicaciones': publicaciones}, {"avatar":obtenerAvatar(request)})

#Función para crear publicaciones
@login_required
def crear_seccion(request):
    avatar=obtenerAvatar(request)
    if request.method == "POST":
        form = crearBlogForm(request.POST, request.FILES)
        if form.is_valid():
            seccion = form.save(commit=False)
            seccion.autor = request.user 
            seccion.save()
            return redirect('inicioComunidad')
    else:
        form = crearBlogForm()

    return render(request, "AppComunidad/crearblog.html", {'form': form}, {"avatar":obtenerAvatar(request)})


#Función para editar publicaciones
@login_required
def editar_seccion(request, comunidad_id):
    avatar=obtenerAvatar(request)
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    if comunidad.autor == request.user:
        if request.method == "POST":
            form = crearBlogForm(request.POST, request.FILES, instance=comunidad)
            if form.is_valid():
                form.save()
                return redirect('contenido')
        else:
            form = crearBlogForm(instance=comunidad)
        
        return render(request, "AppComunidad/editarblog.html", {'form': form, 'comunidad': comunidad}, {"avatar":obtenerAvatar(request)})
    else:
        return HttpResponseForbidden("No tienes permisos para editar esta publicación")


#Función para eliminar publicaciones
@login_required
def eliminar_seccion(request, comunidad_id):
    avatar=obtenerAvatar(request)
    comunidad = get_object_or_404(Comunidad, id=comunidad_id)
    if comunidad.autor == request.user:
        if request.method == "POST" or 'eliminar' in request.POST:
            comunidad.delete()
            return redirect('contenido')
        else:
            return render(request, "AppComunidad/eliminarblog.html", {'comunidad': comunidad} , {"avatar":obtenerAvatar(request)})
    else:
        return HttpResponseForbidden("No tienes permisos para eliminar esta publicación")

@login_required
def ver_mensajes(request, usuario_id):
    receptor = get_object_or_404(User, id=usuario_id)
    mensajes = Mensaje.objects.filter(receptor=receptor, emisor=request.user) | Mensaje.objects.filter(receptor=request.user, emisor=receptor)
    mensajes = mensajes.order_by('fecha_envio')
    form = MensajeForm()
    return render(request, 'chat/ver_mensajes.html', {'receptor': receptor, 'mensajes': mensajes, 'form': form})

@login_required
def enviar_mensaje(request, usuario_id):
    receptor = get_object_or_404(User, id=usuario_id)
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.receptor = receptor
            mensaje.save()
            messages.success(request, 'Mensaje enviado con éxito.')
            return redirect('ver_mensajes', usuario_id=usuario_id)
    else:
        form = MensajeForm()
    return render(request, 'chat/enviar_mensaje.html', {'receptor': receptor, 'form': form})



        