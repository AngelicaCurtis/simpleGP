from django.urls import path

from servidores.views import atualizar_servidor, deletar_servidor, \
    ServidorDetail, ServidorCreate, ServidorUpdate, Delete, servidores_list, HistoricoProgressoes, tipo_sanguineo, \
    servidor_form,  servidor_perfil

urlpatterns = [
    path('lista-servidores/', servidores_list, name="lista-servidores"),
    path('servidor_perfil/', servidor_perfil, name="servidor_perfil"),
    path('tipo-sanguineo/', tipo_sanguineo, name="tipo-sanguineo"),
    path('servidor-detail/<pk>', ServidorDetail.as_view(), name="servidor-detalhes"),
    path('progressoes/<pk>', HistoricoProgressoes.as_view(template_name="servidores/progressoes.html"), name="servidor-progressoes"),
    path('servidor-create/', ServidorCreate.as_view(template_name="servidores/servidor_formulario.html"), name="servidor-form"),
    path('servidor-formulario/', servidor_form, name="servidor-formulario"),
    path('servidor_update_form/<pk>', ServidorUpdate.as_view(), name="servidor-update"),
    path('delete/<pk>', Delete.as_view(template_name="servidores/delete.html"), name="delete"),
    path('atualizar/<int:id>', atualizar_servidor, name="url_atualizar"),
    path('deletar/<int:id>', deletar_servidor, name="url_deletar"),


]
