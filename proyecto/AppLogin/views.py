from django.shortcuts import render, redirect
from django.contrib.auth import *
from .models import *
from .forms import RegistroUsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginHome(request):
    formulario_authenticacion = AuthenticationForm()
    context = {'form' : formulario_authenticacion}

    return render(request, "AppLogin/loginhome.html", context)

def loginUsuario(request):
    if request.method == "POST":
        form=AuthenticationForm (request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario=info["username"]
            contraseña=info["passwords"]
            usuario=authenticate (username=usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return render (request, "AppLogin/loginusuario.html"), {"mensaje": f"Bienvenido {usuario}"}

            else:
                return render (request, "AppLogin/loginusuario.html"), {"mensaje": "Datos Invalidos, reintente"}

        else:
            return render (request, "AppLogin/loginusuario.html"), {"mensaje": "Opción invalida"}

    else:
        form = AuthenticationForm()
    return render(request, "AppLogin/loginusuario.html", {"form": form, "mensaje":mensaje})
    
def registro(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppLogin/loginhome.html", {"mensaje":f" {nombre_usuario} se ha creado sin problemas :)"})
    else:
        form=RegistroUsuarioForm()
        return render(request,"AppLogin/registro.html", {"form":form})
