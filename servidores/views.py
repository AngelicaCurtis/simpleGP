from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from portarias.models import Portaria
from progressoes.models import Progressao
from servidores.forms import ServidorForm
from servidores.models import Servidor


def home(request):
    return render(request, 'servidores/home.html')


#
# @login_required
# def lista_servidores(request):
#
#     servidores = Servidor.objects.all()
#     return render(request, 'servidores/lista-servidores.html', {'servidores': servidores})

# lista usando ListView
# @method_decorator(login_required, name='dispatch')
# class ServidorList(LoginRequiredMixin, ListView):
#
#     model = Servidor
#     object_list: Servidor
#
#     def get_queryset(self):
#         try:
#             name = self.kwargs['busca']
#         except:
#             name = ''
#         if (name != ''):
#             object_list = self.model.objects.filter(name__icontains=name)
#         else:
#             object_list = self.model.objects.all()
#         return object_list


# list(Servidor.objects.all().order_by('nome'))

class ServidorOrder(ListView):
    model = Servidor
    model.objects.all().order_by('nome')


# detalha servidor

class ServidorDetail(DetailView):
    model = Servidor


class ServidorCreate(CreateView):
    model = Servidor
    fields = ['siape', 'nome', 'sobrenome', 'data_nasc', 'sexo', 'tipo_sanguineo', 'email', 'naturalidade',
              'categoria', 'cargo', 'area', 'data_exercicio', 'campus', 'foto']

    success_url = '/servidores/lista-servidores'


class ServidorUpdate(UpdateView):
    model = Servidor
    fields = ['siape', 'nome', 'sobrenome', 'data_nasc', 'sexo', 'tipo_sanguineo', 'email', 'naturalidade',
              'categoria', 'cargo', 'area', 'data_exercicio', 'campus', 'foto']

    def get_success_url(self):  ## retorna apenas em caso de sucesso
        return reverse_lazy('lista-servidores')


class Delete(DeleteView):
    model = Servidor

    def get_success_url(self):  ## retorna apenas em caso de sucesso
        return reverse_lazy('lista-servidores')


# fixme implementar formulario editando campos pelo html
@login_required
def servidores_list(request):
    termo_busca = request.GET.get("busca", None)
    # lista_servidores = Servidor.objects.all()

    if termo_busca:
        lista_servidores = Servidor.objects.filter(nome__icontains=termo_busca) \
                           or Servidor.objects.filter(sobrenome__icontains=termo_busca) \
                           or Servidor.objects.filter(categoria__nome__icontains=termo_busca) \
                           or Servidor.objects.filter(cargo__nome__icontains=termo_busca) \
                           or Servidor.objects.filter(area__nome__icontains=termo_busca)
    else:
        lista_servidores = Servidor.objects.order_by('nome')
    paginator = Paginator(lista_servidores, 5)
    page = request.GET.get('page')
    servidores = paginator.get_page(page)
    return render(request, 'servidores/servidor_list.html', {'servidores': servidores})


@login_required
def tipo_sanguineo(request):
    termo_busca = request.GET.get("busca", None)
    # lista_servidores = Servidor.objects.all()

    if termo_busca:
        lista_servidores = Servidor.objects.filter(nome__icontains=termo_busca) \
                           or Servidor.objects.filter(sobrenome__icontains=termo_busca) \
                           or Servidor.objects.filter(categoria__nome__icontains=termo_busca) \
                           or Servidor.objects.filter(cargo__nome__icontains=termo_busca) \
                           or Servidor.objects.filter(area__nome__icontains=termo_busca)
    else:
        lista_servidores = Servidor.objects.order_by('nome')
    paginator = Paginator(lista_servidores, 5)
    page = request.GET.get('page')
    servidores = paginator.get_page(page)
    return render(request, 'servidores/tipo-sanguineo.html', {'servidores': servidores})


def atualizar_servidor(request, id):
    servidor = get_object_or_404(Servidor, pk=id)
    form = ServidorForm(request.POST or None, request.FILES or None, instance=servidor)

    if form.is_valid():
        form.save()
        return redirect('lista-servidores')
    return render(request, 'servidores/cadastro.html', {'form': form})


def deletar_servidor(request, id):
    servidor = get_object_or_404(Servidor, pk=id)

    if request.method == 'POST':
        servidor.delete()
        return redirect('lista-servidores')
    return render(request, 'servidores/servidor_deletar.html', {'servidor': servidor})


class HistoricoProgressoes(DetailView):
    model = Servidor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.categoria.id in 'DOC':
            context["tipo_progressao_a"] = "Progressões Docente"
            context['progressoes_a'] = Progressao.objects.filter(servidor__id=self.object.id).select_related('portaria')



        elif self.object.categoria.id in 'TAE':
            context["tipo_progressao_a"] = "Progressões por Capacitação Profissional"
            context['progressoes_a'] = Progressao.objects.select_related('portaria').filter(servidor__id=self.object.id)\
                .filter(tipo_progressao_tae=2).order_by('nivel_capacitacao')
            context["tipo_progressao_b"] = "Progressões por Mérito Profissional"
            context['progressoes_b'] = Progressao.objects.select_related('portaria').filter(servidor__id=self.object.id)\
                .filter(tipo_progressao_tae=1).order_by('padrao_tae')


        return context
