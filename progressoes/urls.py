from django.urls import path

from progressoes.views import CadastroTAE, ProgressaoList, Atualizar, Deletar, ProgressaoDetalhes, Historico

urlpatterns = [
    path('cadastro-tae/', CadastroTAE.as_view(template_name="progressoes/cadastro-progressao-tae.html"),
         name="cadastro-progressao-tae"),
    path('lista-tae/', ProgressaoList.as_view(template_name="progressoes/lista-tae.html"), name="lista-tae"),
    path('historico/', Historico.as_view(template_name="progressoes/historico.html"), name="historico"),
    path('atualizar/<pk>', Atualizar.as_view(template_name="progressoes/atualizar.html"), name="atualizar"),
    path('visualizar/<pk>', ProgressaoDetalhes.as_view(template_name="progressoes/historico.html"), name="visualizar"),
    path('deletar/<pk>', Deletar.as_view(template_name="progressoes/delete.html"), name="deletar"),

]
