from django.contrib import admin
from .models import *


# Register your models here.
class OrientadorAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'linhadepesquisa__descricao']
    list_display = ('nome', 'linhadepesquisa', 'get_programa')
# 'linhadepesquisa__programa__nome_diploma',


class LinhaPesquisaAdmin(admin.ModelAdmin):
    search_fields = ['descricao']
    list_display = ('descricao', 'get_programa', 'get_nivel_programa')


class EditalAdmin(admin.ModelAdmin):
    search_fields = ['programa__nome_diploma', 'ano']
    list_display = ('get_num_ano', 'programa', 'url_edital')


admin.site.register(Edital, EditalAdmin)
admin.site.register(Etapa)
admin.site.register(Programa)
admin.site.register(LinhaPesquisa, LinhaPesquisaAdmin)
admin.site.register(Orientador, OrientadorAdmin)
