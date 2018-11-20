# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from portarias.models import Portaria


class PortariaCreate(CreateView):
    model = Portaria
    fields = ['numero', 'ano', 'origem', 'descricao', 'portaria']

    success_url = '/portarias/portaria_formulario'


def portarias_list(request):
    if not request.user.has_perm('servidores.visualizar_servidor'):
        return HttpResponse("Não Autorizado!")
    termo_busca = request.GET.get("busca", None)

    if termo_busca:
        lista_portarias = Portaria.objects.filter(descricao__icontains=termo_busca) \
                           or Portaria.objects.filter(origem__icontains=termo_busca) \
                           or Portaria.objects.filter(numero__icontains=termo_busca) \


    else:
        lista_portarias = Portaria.objects.order_by('ano')
    paginator = Paginator(lista_portarias, 5)
    page = request.GET.get('page')
    portarias = paginator.get_page(page)
    return render(request, 'portarias/portaria_list.html', {'portarias': portarias})