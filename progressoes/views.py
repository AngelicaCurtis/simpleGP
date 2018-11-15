from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from progressoes.models import Progressao
from servidores.models import Servidor


class Cadastro(CreateView):
    model = Progressao

    fields = ["servidor",
              "tipo_progressao_docente",
              "tipo_progressao_tae",
              "classe_docente",
              "nivel_docente",
              "nivel_capacitacao",
              "padrao_tae",
              "data_progressao",
              "carga_horaria_apresentada",
              "homologacao",
              "portaria"]

    success_url = '/progressoes/lista'

    def dispatch(self, request, *args, **kwargs):

        if "servidor_progressao" not in request.session and not request.POST:
            return redirect("selecao")
        else:
            if not request.POST:
                self.initial = {"servidor": request.session["servidor_progressao"]}
                del request.session["servidor_progressao"]

            return super(Cadastro, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO: Verificar se é necessário carregar context (Não precisa carregar quando for submit)
        if self.initial.get('servidor', None):
         context["servidor_data"] = Servidor.objects.get(id=self.initial.get("servidor"))

        return context


class SelecaoServidor(View):
    model = Servidor

    def get(self, request):
        data = {"servidores": Servidor.objects.all()}
        return render(request, 'progressoes/selecao-servidor.html', data)

    def post(self, request):
        request.session["servidor_progressao"] = request.POST['servidor']
        return redirect("cadastro-progressao")


def ProgressaoList(request):
    termo_busca = request.GET.get("busca", None)

    if termo_busca:
        lista_progressoes = Progressao.objects.filter(servidor__nome__icontains=termo_busca)
    else:
        lista_progressoes = Progressao.objects.order_by('data_prox_progressao')

    paginator = Paginator(lista_progressoes, 5)
    page = request.GET.get('page')
    progressoes = paginator.get_page(page)
    return render(request, 'progressoes/lista.html', {'progressoes': progressoes})


class Atualizar(UpdateView):
    model = Progressao
    fields = ['servidor', 'tipo_progressao_docente', 'tipo_progressao_tae', 'classe_docente', 'nivel_docente',
              'nivel_capacitacao',
              'padrao_tae', 'data_progressao', 'portaria',
              'data_prox_progressao']

    def get_success_url(self):  ## retorna apenas em caso de sucesso
        return reverse_lazy('lista')


class Deletar(DeleteView):
    model = Progressao

    def get_success_url(self):  ## retorna apenas em caso de sucesso
        return reverse_lazy('lista')


class ProgressaoDetalhes(DetailView):
    model = Progressao

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servidores'] = Servidor.objects.filter(id=self.object.id)
        return context



class Historico(DetailView):
    pass
