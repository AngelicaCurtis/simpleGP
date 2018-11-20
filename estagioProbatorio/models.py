from django.db import models

from estagioProbatorio import const
from portarias.models import Portaria
from servidores.models import Servidor


class EstagioProbatorio(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    processo = models.CharField(max_length=20)
    portaria_homologacao = models.ForeignKey(Portaria, blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Estágios Probatórios'

    def __str__(self):
        return self.servidor


class Avaliacao(models.Model):
    ordem = models.CharField(choices=const.ORDEM, max_length=1)
    data = models.DateField(null=True, blank=True)
    nota_aval_servidor = models.IntegerField(blank=True, null=True)
    nota_aval_chefia = models.IntegerField(blank=True, null=True)
    media_aval = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    estagio = models.ForeignKey(EstagioProbatorio, on_delete=models.CASCADE, unique=False)
