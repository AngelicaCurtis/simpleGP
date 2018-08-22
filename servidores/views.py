from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from servidores.forms import ServidorForm
from servidores.models import Servidor


def home(request):
    return render(request, 'servidores/home.html')
@login_required
def lista_servidores(request):

    servidores = Servidor.objects.all()

    return render(request, 'servidores/lista.html', {'servidores': servidores})


@login_required
def cadastro_servidor(request):
    form = ServidorForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'servidores/cadastro.html', {'form': form})


@login_required
def atualizar_servidor(request, id):
    servidor = get_object_or_404(Servidor, pk=id)
    form = ServidorForm(request.POST or None, request.FILES or None, instance=servidor)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'servidores/cadastro.html', {'form': form})


@login_required
def deletar_servidor(request, id):
    servidor = get_object_or_404(Servidor, pk=id)

    if request.method == 'POST':
        servidor.delete()
        return redirect('lista')
    return render(request, 'servidores/servidor_deletar.html', {'servidor': servidor})