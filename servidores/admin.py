from django.contrib import admin

from campi.models import Campus
from portarias.models import Portaria
from progressoes.models import Progressao
from servidores.models import Categoria, Servidor, Cargo, Area

admin.site.register(Categoria)
admin.site.register(Cargo)
admin.site.register(Area)
admin.site.register(Servidor)
admin.site.register(Progressao)
admin.site.register(Portaria)
admin.site.register(Campus)

