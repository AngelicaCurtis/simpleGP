from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from estagioProbatorio.models import EstagioProbatorio, Avaliacao
from tipoSanguineo.models import TipoSanguineo
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
admin.site.register(TipoSanguineo)
# admin.site.register(EstagioProbatorio)
admin.site.register(Avaliacao)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ServidorInline(admin.StackedInline):
    model = Servidor
    can_delete = False
    verbose_name_plural = 'servidores'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ServidorInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

