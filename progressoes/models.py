from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from portarias.models import Portaria
from progressoes import const
from servidores.models import Servidor


class ProgressaoDocente(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    tipo_progressao = models.CharField(choices=const.TIPO_PROGRESSAO_DOC, max_length=1)
    classe = models.CharField(choices=const.CLASSE_DOCENTE, max_length=1)
    nivel = models.CharField(choices=const.NIVEL_DOCENTE, max_length=1)
    data_progressao = models.DateField()
    portaria = models.OneToOneField(Portaria, on_delete=models.CASCADE)
    data_prox_progressao = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Progressão Docente'

        unique_together = (("servidor", "tipo_progressao", "classe", "nivel"),)

    def __str__(self):
        return "{} {}, {}/{}".format(self.servidor, self.tipo_progressao, self.classe, self.nivel)



@receiver(pre_save, sender=ProgressaoDocente)
def callback_progressao_docente(sender, instance, *args, **kwargs):
    instance.data_prox_progressao = (instance.data_progressao + relativedelta(years=+2))





class ProgressaoTAE(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    tipo_progressao = models.CharField(choices=const.TIPO_PROGRESSAO_TAE, max_length=1)
    nivel_capacitacao = models.CharField(choices=const.NIVEL_TAE, max_length=1, null=True, blank=True)
    padrao = models.CharField(choices=const.PADRAO_TAE, max_length=1, null=True, blank=True)
    data_progressao = models.DateField()
    portaria = models.OneToOneField(Portaria, on_delete=models.CASCADE)
    data_prox_progressao = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Progressão TAE'

        unique_together = (("servidor", "tipo_progressao", "nivel_capacitacao"), ("servidor", "tipo_progressao", "padrao"))

    def __str__(self):
        return "{} {}, {}/{}".format(self.servidor, self.tipo_progressao, self.nivel_capacitacao, self.padrao)


@receiver(pre_save, sender=ProgressaoTAE)
def callback_progressao_tae(sender, instance, *args, **kwargs):
    instance.data_prox_progressao = (instance.data_progressao + relativedelta(years=+1, month=+6))