from django.forms import ModelForm

from servidores.models import Servidor


class ServidorForm(ModelForm):
    class Meta:
        model = Servidor
        fields = ['siape', 'nome', 'sobrenome', 'data_nasc', 'sexo', 'tipo_sanguineo',
                  'email', 'naturalidade', 'categoria','cargo', 'area', 'foto']
