from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.http import HttpResponseForbidden
from .models import *
from .forms import RegistroUsuarioForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def obtenerAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if len(avatares) != 0:
        return avatares[0].imagen.url
    else:
        return f"{settings.MEDIA_URL}avatars/avatarpordefecto.png"


def loginUsuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, 'Usuario logeado correctamente.')
            return redirect('inicioComunidad')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, reintente.')
    else:
        form = AuthenticationForm()

    return render(request, "AppLogin/loginusuario.html", {"form": form})

    
def registro(request):
    if request.method == 'POST':
        user_form = RegistroUsuarioForm(request.POST)
        avatar_form = AvatarForm(request.POST, request.FILES)
        if user_form.is_valid() and avatar_form.is_valid():
            info = user_form.cleaned_data
            userName = info['username']
            password = info['password1']
            user = user_form.save()
            usuario = authenticate(username=userName, password=password)
            login(request, usuario)
            avatar = Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            messages.success(request, f'Nuevo usuario {userName} creado')
            return redirect('loginusuario')
        else:
            messages.error(request, "Error: Las contraseñas no coinciden o hay un problema en el formulario.")
    else:
        user_form = RegistroUsuarioForm()
        avatar_form = AvatarForm()

    return render(request, "AppLogin/registro.html", {"user_form": user_form, "avatar_form": avatar_form})

@login_required
def editarusuario(request):
    avatar = obtenerAvatar(request)
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cambios guardados exitosamente')
            return redirect('inicioComunidad')
        else:
            messages.error(request, 'Error: Reintente, datos mal ingresados')

    else:
        form = UserEditForm(instance=usuario)

    return render(request, "AppLogin/editarusuario.html", {"form": form, "nombreusuario": usuario.username, "avatar":obtenerAvatar(request)})


def seleccionarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(user=request.user, imagen=request.FILES["imagen"])            
            avatarViejo = Avatar.objects.filter(user=request.user)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
            avatar.save()
            mensaje = "Avatar agregado correctamente"
        else:
            mensaje = "Error al agregar el avatar"
    else:
        form = AvatarForm()
        mensaje = ""

    return render(request, "AppLogin/seleccionaravatar.html", {"form": form, "usuario": request.user, "mensaje": mensaje})
