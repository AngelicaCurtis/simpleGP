from dateutil.relativedelta import relativedelta
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from portarias.models import Portaria
from progressoes import const
from progressoes.const import TIPO_PROGRESSAO_TAE
from servidores.models import Servidor


class Progressao(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    tipo_progressao_docente = models.CharField(choices=const.TIPO_PROGRESSAO_DOCENTE, max_length=2, null=True, blank=True)
    tipo_progressao_tae = models.CharField(choices=TIPO_PROGRESSAO_TAE, max_length=1, null=True, blank=True)
    classe_docente = models.CharField(choices=const.CLASSE_DOCENTE, max_length=1, null=True, blank=True)
    nivel_docente = models.CharField(choices=const.NIVEL_DOCENTE, max_length=1, null=True, blank=True)
    nivel_capacitacao = models.CharField(choices=const.NIVEL_TAE, max_length=1, null=True, blank=True)
    padrao_tae = models.CharField(choices=const.PADRAO_TAE, max_length=2, null=True, blank=True)
    data_progressao = models.DateField()
    carga_horaria_apresentada = models.IntegerField()
    carga_horaria_excedente = models.IntegerField()
    homologacao = models.FileField(upload_to="homologacao", null=True, blank=True)
    portaria = models.OneToOneField(Portaria, on_delete=models.CASCADE)
    data_prox_progressao = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Progressões'

        unique_together = (("servidor", "tipo_progressao_docente", "classe_docente", "nivel_docente"),
                           ("servidor", "tipo_progressao_tae", "nivel_capacitacao"), ("servidor", "tipo_progressao_tae","padrao_tae"))

    def __str__(self):
        return "{} {}, {}/{}".format(self.servidor, self.tipo_progressao_tae or self.tipo_progressao_docente)



@receiver(pre_save, sender=Progressao)
def callback_progressao(sender, instance, *args, **kwargs):
    if instance.tipo_progressao_docente is not None:
        instance.data_prox_progressao = (instance.data_progressao + relativedelta(years=+2))

    elif instance.tipo_progressao_tae is not None:
        instance.data_prox_progressao = (instance.data_progressao + relativedelta(years=+1, months=+6))



