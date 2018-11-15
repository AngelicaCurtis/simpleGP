from django import forms

from servidores.models import Servidor


class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ['categoria', 'siape', 'nome', 'sobrenome', 'data_nasc', 'sexo', 'tipo_sanguineo', 'email', 'naturalidade',
               'cargo', 'area', 'data_exercicio', 'campus', 'foto']
