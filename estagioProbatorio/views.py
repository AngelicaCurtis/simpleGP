from dateutil.relativedelta import relativedelta
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView

from estagioProbatorio.forms import EstagioProbatorioForm, AvaliacaoForm
from estagioProbatorio.models import Avaliacao, EstagioProbatorio


def cadastro_estagio_probatorio(request):
    form = EstagioProbatorioForm(request.POST, None)
    if form.is_valid():

        estagio_probatorio = form.save()

        if estagio_probatorio:
            servidor = estagio_probatorio.servidor

            data_avaliacao = servidor.data_exercicio

            for i in range(4):
                data_avaliacao = data_avaliacao + relativedelta(months=+8)

                nova_avaliacao = Avaliacao.objects.create(
                    ordem=(i + 1),
                    data=data_avaliacao,
                    nota_aval_servidor=None,
                    nota_aval_chefia=None,
                    media_aval=None,
                    status=False,
                    estagio=estagio_probatorio)

                nova_avaliacao.save()

    return render(request, 'estagioProbatorio/estagio_probatorio_formulario.html', {'form': form})


class EstagioProbatorioList(ListView):
    model = EstagioProbatorio


class AvaliacaoUpdate(LoginRequiredMixin, UpdateView):
    model = Avaliacao
    fields = [
        'ordem',
        'data',
        'nota_aval_servidor',
        'nota_aval_chefia',
        'status',
    ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('lista-estagios')


class MeuEstagioProbatorio(ListView):
    pass
