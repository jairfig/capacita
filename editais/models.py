from django.db import models

import os
from datetime import date, datetime
from .validators import validate_file_extension_pdf
from capacita import choices
from programa.models import Programa, OrganizacaoPrograma


# Create your models here.
class Vaga(models.Model):
    edital = models.ForeignKey('Edital', on_delete=models.CASCADE, related_name='vagas_edital')
    item_vaga = models.ForeignKey('programa.OrganizacaoPrograma', on_delete=models.CASCADE, related_name='detalhamento_vagas')
    nivel = models.ForeignKey('programa.Nivel', on_delete=models.CASCADE, related_name='niveis_vaga')
    numero_vagas = models.IntegerField('Número de Vagas para este Item', null=False, blank=False)

    def __str__(self):
        return f'[{self.numero_vagas}] Concorrência {self.item_vaga.nome} - Edital {self.edital.get_num_ano()}/{self.edital.programa.sigla}/{self.nivel}'

    class Meta:
        verbose_name_plural = u'Vagas'


class Arquivo(models.Model):
    edital = models.ForeignKey('Edital', on_delete=models.CASCADE, related_name='arquivos_edital')
    dt_envio = models.DateTimeField(u'Data do Envio', auto_now_add=True, null=True, blank=True)
    descricacao = models.CharField('Descrição do Arquivo', max_length=150, null=False, blank=True)

    def dir_arquivos(self, filename):
        extension = os.path.splitext(filename)[-1]
        return f'arquivos_editais/{self.edital.programa.sigla}/{self.edital.ano}/{self.edital.get_num_ano()}-{self.dt_envio}{extension}'

    arquivo = models.FileField(upload_to=dir_arquivos, storage=None, max_length=120, blank=True, null=True)

    def __str__(self):
        return f'{self.edital} - {self.descricacao}'


class Edital(models.Model):
    programa = models.ForeignKey('programa.Programa', on_delete=models.CASCADE, related_name='editais')
    numero = models.IntegerField('Número do Edital', null=False, blank=False)
    ano = models.CharField('Ano do Edital', choices=choices.ANO_CHOICE, default=date.today().year, null=False, blank=False,
                           max_length=4)
    url_edital = models.CharField('URL do edital no site da ufac', null=True, blank=True, max_length=800)
    concorrencia = models.CharField('Tipo de Concorrência', choices=choices.CONCORRENCIA, max_length=20, default=choices.CONCORRENCIA[0][0])
    nivel_vagas = models.ManyToManyField('programa.Nivel')

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

#
# def path_documento(self, filename):
#     extension = os.path.splitext(filename)[-1]
#     return f'docs_editais/{self.edital.programa.sigla}{self.horario.replace(":","-")}{extension}'
#
#
# class Arquivo(models.Model):
#     edital = models.ForeignKey(Edital, related_name='anexosedital_set', on_delete=models.CASCADE)
#     arquivo = models.FileField('Arquivo', upload_to=path_documento, max_length=250, validators=[validate_file_extension_pdf])
#     dt_envio = models.DateTimeField(u'Data do Envio', auto_now_add=True, null=True, blank=True)
#
#     def __unicode__(self):
#         return u'%s - %s' % (self.edital.get_num_ano(), self.edital.programa.sigla)
#
#     class Meta:
#         unique_together = ['edital']
#         verbose_name_plural = U'Arquivos'
