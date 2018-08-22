from django.db import models


# Create your models here.

from servidores import const


class Categoria (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


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
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)

class Contato(models.Model):
    telefone = models.CharField(max_length=30)
    celular = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    endereco = models.CharField(max_length=200)
    servidor = models.OneToOneField(Servidor, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.celular


class DadosBancarios(models.Model):
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=20)
    conta = models.IntegerField(max_length=10)
    municipio = models.CharField(max_length=200)
    servidor = models.OneToOneField(Servidor, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.banco
class Formacao(models.Model):
    titulacao = models.CharField(choices=const.TITULACAO, max_length=1)
    descricao = models.TextField(max_length=300)
    local = models.CharField(max_length=200)
    data_conclusao = models.DateField()
    area_conhecimento = models.CharField(max_length=100)
    servidor = models.OneToOneField(Servidor, on_delete=models.CASCADE, primary_key=True)
