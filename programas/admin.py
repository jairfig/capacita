from django.contrib import admin
from .models import *


# Register your models here.
class OrientadorAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'linha__descricao']
    list_display = ('nome', 'area_atuacao', 'linha', 'get_programa')


class LinhaPesquisaAdmin(admin.ModelAdmin):
    search_fields = ['descricao']
    list_display = ('descricao', 'get_programa', 'get_nivel_programa')


admin.site.register(Programa)
admin.site.register(Area)
admin.site.register(LinhaPesquisa, LinhaPesquisaAdmin)
admin.site.register(Orientador, OrientadorAdmin)
