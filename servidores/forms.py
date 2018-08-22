from django.contrib.admin import TabularInline
from django.forms import ModelForm, inlineformset_factory


from servidores.models import Servidor


class ServidorForm(ModelForm):
    class Meta:
        model = Servidor
        fields = ['id_unica', 'nome', 'sobrenome','data_nasc', 'sexo', 'tipo_sanguineo', 'cpf',
                  'rg', 'pis_pasep', 'naturalidade', 'categoria', 'foto']

