from django.contrib import admin

from progressoes.models import ProgressaoDocente
from servidores.models import Categoria, Servidor, DadosBancarios, Contato, Formacao


class DadosBancariosInline(admin.TabularInline):
    model = DadosBancarios

class ContatosInline(admin.TabularInline):
    model = Contato

class FormacaoInline(admin.TabularInline):
    model = Formacao



class ServidorAdmin(admin.ModelAdmin):
    inlines = [
        DadosBancariosInline,
        FormacaoInline,
        ContatosInline
    ]

# Register your models here.


admin.site.register(Categoria)
admin.site.register(Servidor, ServidorAdmin)
admin.site.register(ProgressaoDocente)

