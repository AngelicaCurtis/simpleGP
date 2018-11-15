from django.db import models

from estagioProbatorio import const
from servidores.models import Servidor

class Avaliacao(models.Model):
    data = models.DateField()
    nota_aval_servidor = models.IntegerField()
    nota_aval_chefia = models.IntegerField()
    media_aval = models.IntegerField()
    status = models.BooleanField()


class EstagioProbatorio(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    Processo = models.CharField(max_length=20)
    primeira_avaliacao = models.ManyToOneRel(Avaliacao, on_delete=models.PROTECT)
    segunda_avaliacao = models.ManyToOneRel(Avaliacao, on_delete=models.PROTECT)
    terceira_avaliacao = models.ManyToOneRel(Avaliacao, on_delete=models.PROTECT)
    quarta_avaliacao = models.ManyToOneRel(Avaliacao, on_delete=models.PROTECT)


    class Meta:
        verbose_name_plural = 'Estágios Probatórios'

    def __str__(self):
        return self.nome





