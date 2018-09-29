from django.db import models

from campi.models import Campus


class Portaria(models.Model):
    numero = models.CharField(primary_key=True, max_length=4)
    ano = models.SmallIntegerField()
    origem = models.ForeignKey(Campus, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=200)
    portaria = models.FileField(upload_to="portarias", null=True, blank=True)

    class Meta:
        unique_together = (("numero", "ano", "origem"),)

    def __str__(self):
        return "{}/ {}/{}".format(self.numero, self.ano, self.origem)
