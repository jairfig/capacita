from django.contrib import admin

from .models import Candidato, Inscricao, Endereco, Cidade
# Register your models here.

admin.site.register(Candidato)
admin.site.register(Inscricao)
admin.site.register(Endereco)
admin.site.register(Cidade)