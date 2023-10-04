from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import formularioMensaje
from django.contrib.auth import login, authenticate
from django.contrib.auth.password_validation import validate_password
from .models import *
from AppLogin.views import obtenerAvatar
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def vista_chat(request):
    avatar = obtenerAvatar(request)
    form = formularioMensaje() 
    usuarios = User.objects.all()
    mensajes_recibidos = Mensaje.objects.filter(recibido=request.user)
    mensajes_enviados = Mensaje.objects.filter(enviado=request.user) 
    if request.method == 'POST':
        form = formularioMensaje(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            print()
            mensaje = Mensaje(enviado=request.user, recibido=info['recibido'], contenido=info['envio'])
            mensaje.save()
            messages.success(request, "Mensaje enviado")
            form = formularioMensaje()
            return render(request,'AppMensajes/chat.html' ,{"form":form, "mensajes_recibidos":mensajes_recibidos, 'mensajes_enviados': mensajes_enviados, 'usuarios': usuarios,'avatar': obtenerAvatar(request)})
        else:
            messages.error(request, "Mensaje no enviado")
            return render(request, 'AppMensajes/chat.html', {'form': form, 'mensajes_recibidos': mensajes_recibidos, 'mensajes_enviados': mensajes_enviados, 'usuarios': usuarios, 'avatar': obtenerAvatar(request)})

    return render(request, 'AppMensajes/chat.html', {'form': form, 'mensajes_recibidos': mensajes_recibidos, 'usuarios': usuarios, 'avatar': obtenerAvatar(request)})


@login_required
def vmsm(request, id):
    avatar = obtenerAvatar(request)
    mensaje = get_object_or_404(Mensaje, pk=id)
    return render(request, 'AppMensajes/verchat.html', {'mensaje': mensaje, 'mensajes_recibidos':mensajes_recibidos, 'avatar': obtenerAvatar(request)})


@login_required
def visualm(request, id):
    avatar = obtenerAvatar(request)
    vm = Mensaje.objects.get(id=id)
    if request.method == 'POST' and vm:
        return redirect( 'chat' )     
    else:        
        return render(request, 'AppMensajes/verchat.html', {'vm': vm, 'avatar': obtenerAvatar(request)})