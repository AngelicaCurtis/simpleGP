from django.db import models

from campi.models import Campus
from servidores import const
from servidores.models import Servidor, Categoria


class TipoSanguineo(models.Model):
    tipo_sanguineo = models.CharField("Tipo Sanguíneo", choices=const.TIPO_SANGUINEO, max_length=1)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    texto_email = models.TextField(max_length=2000)

