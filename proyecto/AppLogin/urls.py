from django.urls import path
from AppLogin import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('loginusuario/', loginUsuario, name="loginusuario"),
        path('registro/', registro, name="registro"),
        path('logoutusuario/', LogoutView.as_view(template_name="AppLogin/logoutusuario.html")),
        path('editarusuario/', editarusuario, name="editarusuario"),
        path('seleccionaravatar/', seleccionarAvatar, name="seleccionaravatar"),
]