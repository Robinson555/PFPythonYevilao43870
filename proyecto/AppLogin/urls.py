from django.urls import path
from .views import *
from AppLogin import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('loginhome/', loginHome, name="loginhome"),
        path('loginusuario/', loginUsuario, name="loginusuario"),
        path('registro/', registro, name="registro"),
        path('logoutusuario/', LogoutView.as_view(template_name="AppLogin/logoutusuario.html")),
]