from django.forms import ModelForm
from django import forms

from progressoes.models import Progressao


class ProgressaoForm(forms.ModelForm):
    class Meta:
        model = Progressao
        fields = {
            "servidor",
            "tipo_progressao_docente",
            "tipo_progressao_tae",
            "classe_docente",
            "nivel_docente",
            "nivel_capacitacao",
            "padrao_tae",
            "data_progressao",
            "portaria",
            "data_prox_progressao"
        }
