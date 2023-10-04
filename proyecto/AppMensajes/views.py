from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import formularioMensaje
from django.contrib.auth import login, authenticate
from django.contrib.auth.password_validation import validate_password
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def vista_chat(request):
    form = formularioMensaje() 
    mensajes_recibidos = Mensaje.objects.filter(recibido=request.user)
    if request.method == 'POST':
        form = formularioMensaje(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            mensaje = Mensaje(enviado=request.user, recibido=info['recibido'], contenido=info['envio'])
            mensaje.save()
            messages.success(request, "Mensaje enviado")
            form = formularioMensaje()
            return redirect('chat')
        else:
            messages.error(request, "Mensaje no enviado")

    return render(request, 'AppMensajes/chat.html', {'form': form, 'mensajes_recibidos': mensajes_recibidos})

@login_required
def vmsm(request, id):
    mensaje = get_object_or_404(Mensaje, pk=id)
    return render(request, 'AppMensajes/verchat.html', {'mensaje': mensaje})