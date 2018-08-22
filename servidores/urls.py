from django.contrib import admin
from django.urls import path
from servidores.views import lista_servidores, cadastro_servidor, atualizar_servidor, deletar_servidor

urlpatterns = [
    path('lista/', lista_servidores, name="lista"),
    path('cadastro/', cadastro_servidor, name="url_cadastro"),
    path('atualizar/<int:id>', atualizar_servidor, name="url_atualizar"),
    path('deletar/<int:id>', deletar_servidor, name="url_deletar")

]
