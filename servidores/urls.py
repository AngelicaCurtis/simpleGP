from django.contrib import admin
from django.urls import path
from servidores.views import atualizar_servidor, deletar_servidor, ServidorList, \
    ServidorDetail, ServidorCreate, ServidorUpdate, Delete, selecao

urlpatterns = [
    path('lista-servidores/', ServidorList.as_view(), name="lista-servidores"),
    path('lista-ordenada/', ServidorList.as_view(template_name="servidores/lista-ordenada.html"), name="lista-ordenada"),
    path('servidor-detail/<pk>', ServidorDetail.as_view(), name="servidor-detalhes"),
    path('servidor-create/', ServidorCreate.as_view(), name="servidor-form"),
    path('servidor_update_form/<pk>', ServidorUpdate.as_view(), name="servidor-update"),
    path('delete/<pk>', Delete.as_view(template_name="servidores/delete.html"), name="delete"),
    path('atualizar/<int:id>', atualizar_servidor, name="url_atualizar"),
    path('deletar/<int:id>', deletar_servidor, name="url_deletar"),
    path('docente/', selecao, name="selecao"),

]
