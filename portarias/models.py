from django.db import models

# Create your models here.
from django.db.models import Model

class Portaria(models.Model):
    numero = models.CharField(primary_key=True, max_length=4)
    ano = models.SmallIntegerField()
    origem = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)

    class Meta:
        unique_together = (("numero", "ano", "origem"),)






