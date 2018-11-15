from django.shortcuts import render
from django.views.generic import CreateView

import tipoSanguineo


class ServidorCreate(CreateView):
    model = tipoSanguineo
    fields = ["all"]
    success_url = '/tipoSanguineo/formulario'
