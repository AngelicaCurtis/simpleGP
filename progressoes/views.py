from django.shortcuts import render
from django.views.generic import CreateView

from progressoes.models import ProgressaoTAE


class CadastroTAE(CreateView):
    model = ProgressaoTAE
    fields = ['servidor', 'tipo_progressao', 'nivel_capacitacao', 'padrao', 'data_progressao', 'portaria',
              'data_prox_progressao',
              ]

    success_url = '/servidores/lista-servidores'
