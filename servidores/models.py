from django.db import models

from servidores import const


class Categoria(models.Model):
    CATEGORIAS = (
        ('1', 'Docente'),
        ('2', 'TAE'),
        ('3', 'Professor Substituto'),
        ('4', 'TAE Exercício Provisório'),
        ('5', 'Docente Exercício Provisório')

    )
    nome = models.CharField(choices=CATEGORIAS, max_length=30, unique=True)
    descricao = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.nome

class Cargo(models.Model):

    nivel = models.CharField("Nível", max_length=1)
    nome = models.CharField("cargo", max_length=200, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField("Área", max_length=200, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome



# TODO melhorar modelagem
class Servidor(models.Model):
    siape = models.CharField("SIAPE", max_length=7, unique=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=200)
    data_nasc = models.DateField("Data de Nascimento")
    sexo = models.CharField(choices=const.SEXO, max_length=1)
    tipo_sanguineo = models.CharField("Tipo Sanguíneo", choices=const.TIPO_SANGUINEO, max_length=1)
    email = models.EmailField("E-mail")
    naturalidade = models.CharField(max_length=200)
    foto = models.ImageField("Foto Perfil", upload_to="fotos_servidores", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Servidores'

        unique_together = (
            ("siape", "nome", "cargo"), ("siape", "nome", "area"))

    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)


