from django.contrib import admin

from campi.models import Campus
from portarias.models import Portaria
from progressoes.models import ProgressaoDocente, ProgressaoTAE
from servidores.models import Categoria, Servidor, Cargo, Area

admin.site.register(Categoria)
admin.site.register(Cargo)
admin.site.register(Area)
admin.site.register(Servidor)
admin.site.register(ProgressaoDocente)
admin.site.register(Portaria)
admin.site.register(Campus)
admin.site.register(ProgressaoTAE)
