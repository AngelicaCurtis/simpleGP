from django.urls import path

from estagioProbatorio.views import cadastro_estagio_probatorio, EstagioProbatorioList, AvaliacaoUpdate, MeuEstagioProbatorio

urlpatterns = [
    path('cadastro_estagio', cadastro_estagio_probatorio, name='cadastro-estagio-probatorio'),
    path('lista_estagios/', EstagioProbatorioList.as_view(template_name="estagioProbatorio/lista_estagios.html"),
         name="lista-estagios"),
    path('lista_estagios/', MeuEstagioProbatorio.as_view(template_name="estagioProbatorio/lista_estagios.html"),
         name="meu-estagio"),
    path('avaliacao/<pk>', AvaliacaoUpdate.as_view(), name="atualizar-avaliacao"),

]
