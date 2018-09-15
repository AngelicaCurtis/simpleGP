from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from progressoes.models import ProgressaoTAE


class CadastroTAE(CreateView):
    model = ProgressaoTAE
    fields = ['servidor', 'tipo_progressao', 'nivel_capacitacao', 'padrao', 'data_progressao', 'portaria',
              'data_prox_progressao']

    success_url = '/progressoes/lista-tae'


class ProgressaoList(ListView):
    model = ProgressaoTAE

    ProgressaoTAE = ProgressaoTAE.objects.order_by('nome')

    # def get(self, request, *args, **kwargs):
    #     ProgressaoTAE.objects.filter(servidor__icontains=("Angelica"))


class Historico(ListView):
    model = ProgressaoTAE


class Atualizar(UpdateView):
    model = ProgressaoTAE
    fields = ['servidor', 'tipo_progressao', 'nivel_capacitacao', 'padrao', 'data_progressao', 'portaria',
              'data_prox_progressao']

    def get_success_url(self):  ## retorna apenas em caso de sucesso
        return reverse_lazy('lista-tae')


class Deletar(DeleteView):
    model = ProgressaoTAE

    def get_success_url(self):  ## retorna apenas em caso de sucesso
        return reverse_lazy('lista-tae')


class ProgressaoDetalhes(DetailView):
    model = ProgressaoTAE
