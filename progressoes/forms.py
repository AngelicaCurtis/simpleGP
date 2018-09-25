from django.forms import ModelForm

from progressoes.models import Progressao


class ProgressaoForm(ModelForm):
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
