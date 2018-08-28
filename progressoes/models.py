from django.forms import models


class Servidor(models.Model):
    id_unica = models.CharField("Identidade Única", primary_key=True, max_length=9)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=200)
    data_nasc = models.DateField()
    sexo = models.CharField(choices=const.SEXO, max_length=1)
    tipo_sanguineo = models.CharField(choices=const.TIPO_SANGUINEO, max_length=1)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
    pis_pasep = models.CharField(max_length=13)
    naturalidade = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="fotos_servidores", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)


    class Meta:
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)