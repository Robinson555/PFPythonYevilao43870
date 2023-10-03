from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('messages/', messages_view, name='messages'),
    path('vmsm//<id>/', vmsm, name='vmsm')
]
