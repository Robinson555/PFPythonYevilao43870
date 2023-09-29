from django.urls import path
from AppLogin.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('loginusuario/', loginUsuario, name="loginusuario"),
        path('registro/', registro, name="registro"),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('editarusuario/', editarusuario, name="editarusuario"),
        path('seleccionaravatar/', seleccionarAvatar, name="seleccionaravatar"),
]