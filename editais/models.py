from django.db import models

import os
from datetime import date
from capacita import choices
from programas.models import Programa


# Create your models here.
class Edital(models.Model):
    numero = models.IntegerField('Número do Edital', null=False, blank=False)
    ano = models.CharField('Ano do Edital', choices=choices.ANO_CHOICE, default=date.today().year, null=False, blank=False,
                           max_length=4)
    url_edital = models.CharField('URL do edital no site da ufac', null=True, blank=True, max_length=800)
    programa = models.ForeignKey('programas.Programa', on_delete=models.CASCADE, related_name='editais')
    # nro_vagas = models.IntegerField("Número de Vagas", null=False, blank=False)

    def get_num_ano(self):
        return ' nº ' + self.numero.__str__() + '/' + self.ano

    class Meta:
        ordering = ["-ano"]
        verbose_name_plural = u'Editais'


class Etapa(models.Model):
    etapa = models.CharField('Descrição da etapa', null=True, blank=True, max_length=120)
    dt_inicio = models.DateField('Início')
    dt_fim = models.DateField('Término')
    edital = models.ForeignKey("Edital", on_delete=models.CASCADE, related_name='etapas')

    def __str__(self):
        return self.edital.programa.sigla + ' - ' + self.etapa + ' de ' \
               + self.dt_inicio.strftime('%d/%m/%Y').__str__() + ' a ' \
               + self.dt_fim.strftime('%d/%m/%Y').__str__()


class Arquivo(models.Model):

    def dir_arquivos(self, filename):
        extension = os.path.splitext(filename)[-1]
        return u'%s/%s/%s_%s%s' % ('arquivos_inscricao', self.ano, self.edicao, self.dataHora, extension)

    descricacao = models.CharField('Descrição do Arquivo', max_length=150, null=False, blank=True)
    arquivo = models.FileField(upload_to=dir_arquivos, storage=None, max_length=120, blank=True, null=True)


class ArquivoEtapa(models.Model):
    etapa = models.ForeignKey(Etapa, verbose_name='etapa', related_name='etapa_edital', on_delete=models.CASCADE)
    arquivo = models.ManyToManyField(Arquivo)
