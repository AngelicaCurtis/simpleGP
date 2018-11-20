from django.contrib.auth.models import AbstractUser
from django.db import models

from servidores.models import Servidor


class User(AbstractUser):
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE, null=True, blank=True)

