
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsável, nome referência
    # usuarios.com
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
