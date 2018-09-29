from datetime import date

from django.db.models.signals import pre_save
from django.dispatch import receiver

from servidores.models import Servidor


@receiver(pre_save, sender=Servidor)
def callback_servidor(sender, instance, *args, **kwargs):
    instance.tempo_servico = abs((date.today() - Servidor.data_exercicio))