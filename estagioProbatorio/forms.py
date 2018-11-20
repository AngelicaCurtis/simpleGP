from django.forms import ModelForm
from django import forms

from estagioProbatorio.models import EstagioProbatorio, Avaliacao


class EstagioProbatorioForm(forms.ModelForm):
    class Meta:
        model = EstagioProbatorio
        fields = {
            "servidor",
            "processo",
            "portaria_homologacao"
        }

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = {
            "ordem",
            "data",
            "nota_aval_servidor",
            "nota_aval_chefia",
            "status",
            "estagio"
        }

