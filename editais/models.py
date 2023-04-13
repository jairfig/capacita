from django.db import models

import os
from datetime import date
from capacita import choices
from programas.models import Programa


# Create your models here.
class Arquivo(models.Model):

    def dir_arquivos(self, filename):
        extension = os.path.splitext(filename)[-1]
        return u'%s/%s/%s_%s%s' % ('arquivos_inscricao', self.ano, self.edicao, self.dataHora, extension)

    descricacao = models.CharField('Descrição do Arquivo', max_length=150, null=False, blank=True)
    arquivo = models.FileField(upload_to=dir_arquivos, storage=None, max_length=120, blank=True, null=True)


class Vaga(models.Model):
    edital = models.ForeignKey('Edital', on_delete=models.CASCADE, related_name='edital')
    concorrencia = models.CharField('Tipo de Concorrência', choices=choices.CONCORRENCIA, max_length=2, default=choices.CONCORRENCIA[0][0])
    quantidade = models.IntegerField('Total de Vagas do Edital', null=False, blank=False)
    # relacao = models.IntegerField('Vinculo da Vaga', null=False, blank=False)

    def __str__(self):
        return f' São {self.quantidade} vagas para o {self.edital}'


class DetalhamentoVaga(models.Model):
    tipo_concorrencia =  models.ForeignKey('Vaga', on_delete=models.CASCADE, related_name='detalhamento_vagas')
    numero_vagas = models.IntegerField('Total de Vagas do Edital', null=False, blank=False)
    codigo = models.IntegerField('Total de Vagas do Edital', null=False, blank=False)


class Edital(models.Model):
    numero = models.IntegerField('Número do Edital', null=False, blank=False)
    ano = models.CharField('Ano do Edital', choices=choices.ANO_CHOICE, default=date.today().year, null=False, blank=False,
                           max_length=4)
    url_edital = models.CharField('URL do edital no site da ufac', null=True, blank=True, max_length=800)
    programa = models.ForeignKey('programas.Programa', on_delete=models.CASCADE, related_name='editais')
    anexos = models.ManyToManyField(Arquivo, blank=True)

    def get_num_ano(self):
        return self.numero.__str__() + '/' + self.ano

    class Meta:
        ordering = ["-ano"]
        verbose_name_plural = u'Editais'

    def __str__(self):
        return self._meta.object_name + ' ' + self.get_num_ano() + ' ' + self.programa.sigla


class Fase(models.Model):
    edital = models.ForeignKey("Edital", on_delete=models.CASCADE, related_name='fases')
    descricao = models.CharField('Descrição da fase/etapa', null=True, blank=True, max_length=120)
    dt_inicio = models.DateField('Início')
    dt_fim = models.DateField('Término')

    def __str__(self):
        return self.edital.programa.sigla + ' - ' + self.descricao + ' de ' \
               + self.dt_inicio.strftime('%d/%m/%Y').__str__() + ' a ' \
               + self.dt_fim.strftime('%d/%m/%Y').__str__()
