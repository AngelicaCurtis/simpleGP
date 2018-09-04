from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from servidores import const
from servidores.forms import ServidorForm
from servidores.models import Servidor, Categoria


def home(request):
    return render(request, 'servidores/home.html')
#
# @login_required
# def lista_servidores(request):
#
#     servidores = Servidor.objects.all()
#     return render(request, 'servidores/lista-servidores.html', {'servidores': servidores})

# lista usando ListView
@method_decorator(login_required, name='dispatch')
class ServidorList(LoginRequiredMixin, ListView):

    model = Servidor
# list(Servidor.objects.all().order_by('nome'))

class ServidorOrder(ListView):
    model = Servidor
    model.objects.all().order_by('nome')


# detalha servidor

class ServidorDetail(DetailView):
    model = Servidor


class ServidorCreate(CreateView):
    model = Servidor
    fields = ['id_unica', 'nome', 'sobrenome', 'data_nasc', 'sexo', 'tipo_sanguineo', 'cpf',
              'rg', 'pis_pasep', 'naturalidade', 'categoria', 'foto']

    success_url = '/servidores/lista-servidores'

class ServidorUpdate(UpdateView):
    model = Servidor
    fields = ['id_unica', 'nome', 'sobrenome', 'data_nasc', 'sexo', 'tipo_sanguineo', 'cpf',
              'rg', 'pis_pasep', 'naturalidade', 'categoria', 'foto']

    def get_success_url(self): ## retorna apenas em caso de sucesso
        return reverse_lazy('lista-servidores')

class Delete(DeleteView):
    model = Servidor
    def get_success_url(self): ## retorna apenas em caso de sucesso
        return reverse_lazy('lista-servidores')


#fixme implementar formulario editando campos pelo html
@login_required
class CadastroServidor(View):
    def post(self, request):
        data= {}
        data['form_item'] = ServidorForm()
        data['id_unica'] = request.POST['id_unica']
        data['nome'] = request.POST['nome']
        data['sobrenome'] = request.POST['sobrenome']
        data['data_nasc'] = request.POST['data_nasc']
        data['sexo'] = request.POST['sexo']
        data['tipo_sanguineo'] = request.POST['tipo_sanguineo']
        data['cpf'] = request.POST['cpf']
        data['rg'] = request.POST['rg']
        data['pis_pasep'] = request.POST['pis_pasep']
        data['naturalidade'] = request.POST['naturalidade']
        data['foto'] = request.POST['foto']





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

def selecao(request):
    servidores = ServidorForm.objects.filter(categoria="Docente")

    return render(request, 'servidores/docente.html', {servidores})