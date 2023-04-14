from django.contrib import admin
from .models import *


# Register your models here.
class EditalAdmin(admin.ModelAdmin):
    search_fields = ['programa__nome_diploma', 'ano']
    list_display = ('programa', 'edital', 'url_edital')

    def edital(self, obj: Edital) -> str:
        return obj.get_num_ano()

admin.site.register(Edital, EditalAdmin)
admin.site.register(Fase)
admin.site.register(Vaga)
admin.site.register(Arquivo)