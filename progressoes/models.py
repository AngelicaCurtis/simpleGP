from django.db import models

from portarias.models import Portaria
from progressoes import const
from servidores.models import Servidor


class ProgressaoDocente(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    tipo_progressao = models.CharField(choices=const.TIPO_PROGRESSAO_DOC, max_length=1)
    data_progressao = models.DateField()
    portaria = models.OneToOneField(Portaria, on_delete=models.CASCADE)
    data_prox_progressao = models.DateField()

    class Meta:
        verbose_name_plural = 'Progressão Docente'

    def __str__(self):
        return "{} {}".format(self.servidor, self.tipo_progressao)