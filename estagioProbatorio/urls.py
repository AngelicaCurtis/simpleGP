from django.urls import path

from estagioProbatorio.views import cadastro_estagio_probatorio, EstagioProbatorioList, AvaliacaoUpdate

urlpatterns = [
    path('cadastro_estagio', cadastro_estagio_probatorio, name='cadastro-estagio-probatorio'),
    path('lista_estagios/', EstagioProbatorioList.as_view(template_name="estagioProbatorio/lista_estagios.html"),
         name="lista-estagios"),
    path('avaliacao/<pk>', AvaliacaoUpdate.as_view(), name="atualizar-avaliacao"),

]
