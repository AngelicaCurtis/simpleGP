from django.urls import path

from progressoes.views import Cadastro, ProgressaoList, Atualizar, Deletar, ProgressaoDetalhes, SelecaoServidor

urlpatterns = [
    path('cadastro/', Cadastro.as_view(template_name="progressoes/cadastro-progressao.html"),
         name="cadastro-progressao"),
    # path('lista-tae/', ProgressaoList.as_view(template_name="progressoes/lista.html"), name="lista-tae"),
    path('lista/', ProgressaoList, name="lista"),
    path('selecao/', SelecaoServidor.as_view(), name="selecao"),
    path('atualizar/<pk>', Atualizar.as_view(template_name="progressoes/atualizar.html"), name="atualizar"),
    path('visualizar/<pk>', ProgressaoDetalhes.as_view(template_name="progressoes/detalhes.html"), name="visualizar"),
    path('deletar/<pk>', Deletar.as_view(template_name="progressoes/delete.html"), name="deletar"),

]
