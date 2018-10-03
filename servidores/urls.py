from django.urls import path

from servidores.views import atualizar_servidor, deletar_servidor, \
    ServidorDetail, ServidorCreate, ServidorUpdate, Delete, servidores_list, HistoricoProgressoes, tipo_sanguineo

urlpatterns = [
    # path('lista-servidores/', ServidorList.as_view(), name="lista-
    path('lista-servidores/', servidores_list, name="lista-servidores"),
    path('tipo-sanguineo/', tipo_sanguineo, name="tipo-sanguineo"),
    # path('lista-ordenada/', ServidorList.as_view(template_name="servidores/lista-ordenada.html"),
    #      name="lista-ordenada"),
    path('servidor-detail/<pk>', ServidorDetail.as_view(), name="servidor-detalhes"),
    path('progressoes/<pk>', HistoricoProgressoes.as_view(template_name="servidores/progressoes.html"), name="servidor-progressoes"),
    path('servidor-create/', ServidorCreate.as_view(), name="servidor-form"),
    # path('servidor-cadastro/', CadastroServidor.as_view(), name="servidor-cadastro"),
    path('servidor_update_form/<pk>', ServidorUpdate.as_view(), name="servidor-update"),
    path('delete/<pk>', Delete.as_view(template_name="servidores/delete.html"), name="delete"),
    path('atualizar/<int:id>', atualizar_servidor, name="url_atualizar"),
    path('deletar/<int:id>', deletar_servidor, name="url_deletar"),


]
