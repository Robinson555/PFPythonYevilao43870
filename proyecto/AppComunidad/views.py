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
from .forms import crearBlogForm, crearForoForm, comentarioForm, comentarioPregunta
from .models import Comunidad, PreguntasCom, Comentario, ComentarioPregunta

# Create your views here.
@login_required
def inicioComunidad(request):
    avatar= obtenerAvatar(request)
    publicaciones = Comunidad.objects.all()
    preguntas = PreguntasCom.objects.all()

    return render(request,"AppComunidad/homecomunidad.html", {"publicaciones":publicaciones, "preguntas":preguntas, "avatar":obtenerAvatar(request)})

@login_required
def aboutMe(request):
    avatar= obtenerAvatar(request)

    return render(request, "AppComunidad/aboutme.html", {"avatar":obtenerAvatar(request)})
    


#Sección del Blog

@login_required
def contenido(request, comunidad_id):
    avatar=obtenerAvatar(request)
    publicacion = get_object_or_404(Comunidad, id=comunidad_id)
    comentarios = Comentario.objects.filter(publicacion=publicacion)
    
    es_autor = publicacion.autor == request.user
    
    if request.method == 'POST':
        formulario = comentarioForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.autor = request.user
            comentario.publicacion = publicacion
            
            try:
                avatar_usuario = Avatar.objects.get(user=request.user)
                comentario.avatar = avatar_usuario.imagen
            except Avatar.DoesNotExist:
                comentario.avatar = None
            
            respuesta_a_id = request.POST.get('respuesta_a')
            if respuesta_a_id:
                comentario.respuesta_a_id = respuesta_a_id
            
            comentario.save()
            return redirect('contenido', comunidad_id=comunidad_id)
    else:
        formulario = comentarioForm()

    return render(request, "AppComunidad/contenido.html", {'publicacion': publicacion, 'comentarios': comentarios, 'formulario': formulario, 'es_autor': es_autor, 'avatar':obtenerAvatar(request)})

@login_required
def contenidoHome(request):
    avatar=obtenerAvatar(request)
    publicaciones = Comunidad.objects.all()

    success_messages = messages.get_messages(request)

    return render(request, "AppComunidad/contenidohome.html", {'publicaciones':publicaciones, 'avatar':obtenerAvatar(request)})

@login_required
def foroHome(request):
    avatar = obtenerAvatar(request)
    preguntas = PreguntasCom.objects.all()

    success_messages = messages.get_messages(request)

    return render(request, "AppComunidad/forohome.html", {'preguntas': preguntas, 'avatar':obtenerAvatar(request)})

@login_required
def foro(request, preguntas_id):
    avatar = obtenerAvatar(request)
    pregunta = get_object_or_404(PreguntasCom, id=preguntas_id)
    comentariosp = ComentarioPregunta.objects.filter(publicacion=pregunta, respuesta_a=None)  # Obtener comentarios principales sin respuesta_a

    es_autor = pregunta.autor == request.user

    if request.method == 'POST':
        formulario = comentarioPregunta(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.autor = request.user
            comentario.publicacion = pregunta

            try:
                avatar_usuario = Avatar.objects.get(user=request.user)
                comentario.avatar = avatar_usuario.imagen
            except Avatar.DoesNotExist:
                comentario.avatar = None

            respuesta_a_id = request.POST.get('respuesta_a')
            if respuesta_a_id:
                comentario.respuesta_a = ComentarioPregunta.objects.get(id=respuesta_a_id)

            comentario.save()
            return redirect('foro', preguntas_id=preguntas_id)
    else:
        formulario = comentarioPregunta()

    return render(request, "AppComunidad/foro.html", {'pregunta': pregunta, 'comentariosp': comentariosp, 'formulario': formulario, 'es_autor': es_autor, 'avatar': avatar})

#Pagina en proceso de creación
@login_required
def novedades(request):

    en_novedades = True
    return render(request, 'AppComunidad/novedades.html', {'en_novedades': en_novedades})


#Función para crear publicaciones
@login_required
def crear_seccion(request):
    avatar=obtenerAvatar(request)
    if request.method=="POST":
        form=crearBlogForm(request.POST, request.FILES)
        if form.is_valid():
            seccion=form.save(commit=False)
            seccion.autor=request.user 
            seccion.save()
            success_messages = messages.get_messages(request)
            return redirect('contenido', comunidad_id=seccion.id)
    else:
        form = crearBlogForm()

    return render(request, "AppComunidad/crearblog.html", {'form': form, "avatar":obtenerAvatar(request)})

@login_required
def crear_foro(request):
    avatar = obtenerAvatar(request)
    if request.method == 'POST':
        formulario = crearForoForm(request.POST, request.FILES)
        if formulario.is_valid():
            pregunta = formulario.save(commit=False)
            pregunta.autor = request.user
            pregunta.save()
            messages.success(request, 'Publicación creada!')
            return redirect('foro', preguntas_id=pregunta.id)
    else:
        formulario = crearForoForm()

    return render(request, "AppComunidad/crearforo.html", {'formulario': formulario, 'avatar': obtenerAvatar(request)})



#Función para editar publicaciones
@login_required
def editar_seccion(request, comunidad_id):
    avatar=obtenerAvatar(request)
    publicacion = get_object_or_404(Comunidad, id=comunidad_id)
    if publicacion.autor == request.user:
        if request.method == "POST":
            form = crearBlogForm(request.POST, request.FILES, instance=publicacion)
            if form.is_valid():
                form.save()
                messages.success(request, 'La publicación se ha guardado correctamente.')
                return redirect('contenido', comunidad_id=publicacion.id)
        else:
            form = crearBlogForm(instance=publicacion)
        
        return render(request, "AppComunidad/editarblog.html", {'form': form, 'publicacion': publicacion, "avatar":obtenerAvatar(request)})


@login_required
def editar_foro(request, preguntas_id):
    avatar = obtenerAvatar(request)
    pregunta = get_object_or_404(PreguntasCom, id=preguntas_id)    
    if pregunta.autor == request.user:
        if request.method == "POST":
            formulario = crearForoForm(request.POST, request.FILES, instance=pregunta)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, 'El contenido se ha editado correctamente.')
                return redirect('forohome', preguntas_id=preguntas_id)
        else:
            formulario = crearForoForm(instance=pregunta)
        
        return render(request, "AppComunidad/editarforo.html", {'formulario': formulario, 'pregunta': pregunta, "avatar":obtenerAvatar(request)})


#Función para eliminar publicaciones
@login_required
def eliminar_seccion(request, comunidad_id):
    avatar = obtenerAvatar(request)
    publicacion = get_object_or_404(Comunidad, id=comunidad_id)

    if publicacion.autor == request.user:
        if request.method == "POST" and 'eliminar' in request.POST:
            publicacion.delete()
            messages.success(request, 'La publicación fue eliminada.')

            if publicacion.id is not None:
                return redirect('contenidohome', comunidad_id=publicacion.id)
        else:
            return render(request, "AppComunidad/eliminarblog.html", {'publicacion': publicacion, 'avatar':obtenerAvatar(request)})


@login_required
def eliminar_foro(request, preguntas_id):
    avatar = obtenerAvatar(request)
    pregunta = get_object_or_404(PreguntasCom, id=preguntas_id)
    
    if pregunta.autor == request.user:
        if request.method == "POST" or 'eliminar' in request.POST:
            pregunta.delete()
            messages.success(request, 'La publicación fue eliminada.')
            return redirect('forohome')
        else:
            return render(request, "AppComunidad/eliminarforo.html", {'pregunta': pregunta, "avatar": obtenerAvatar(request)})
    else:
        return HttpResponse('No tienes permisos para eliminar esta publicación.')
    


        