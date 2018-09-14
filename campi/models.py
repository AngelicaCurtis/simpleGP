from django.db import models


# Create your models here.

class Campus(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Campi'

    def __str__(self):
        return self.nome
