from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import *
from .forms import RegistroUsuarioForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def loginHome(request):
    formulario_authenticacion = AuthenticationForm()
    context = {'form' : formulario_authenticacion}

    return render(request, "AppLogin/loginhome.html", context)

def loginUsuario(request):
    form=AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = info["username"]
            contraseña = info["password"]
            usuario = authenticate(username=usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                avatar=seleccionarAvatar(request)
                messages.success(request,'User Logged')
                print(messages.success)
                return render(request, "AppComunidad/homecomunidad.html",{"mensaje": f"{usuario} se ha creado sin problemas","avatar":avatar})
            else:
                return render(request, "AppLogin/loginusuario.html",{"mensaje": "Datos Inválidos, reintente","form":form})
        else:
            return render(request, "AppLogin/loginusuario.html",{"mensaje":"Opción inválida","form":form})
    else:
        return render(request, "AppComunidad/homecomunidad.html", {"form": form})
    

def registro(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppLogin/loginusuario.html", {"mensaje":f" {nombre_usuario} se ha creado sin problemas)"})
        else:
            return render(request, "AppLogin/registro.html", {"form":form, "mensaje":"Datos invalidos"})

    else:
        form=RegistroUsuarioForm()
        return render(request,"AppLogin/registro.html", {"form":form})

@login_required
def editarusuario(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppLogin/loginusuario.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppLogin/editarusuario.html", {"form": form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppLogin/editarusuario.html", {"form": form, "nombreusuario":usuario.username})


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