from django.db import models

import os
from datetime import date
from .choices import anos, niveis_programa


# Create your models here.
class Edital(models.Model):
    numero = models.IntegerField('Número do Edital', null=False, blank=False)
    ano = models.CharField('Ano do Edital', choices=anos, default=date.today().year, null=False, blank=False,
                           max_length=4)
    url_edital = models.CharField('URL do edital no site da ufac', null=True, blank=True, max_length=800)
    programa = models.ForeignKey("Programa", on_delete=models.CASCADE, related_name='editais')

    def __str__(self):
        return self.programa.sigla + ' nº ' + self.numero.__str__() + '/' + self.ano

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


class Programa(models.Model):
    cod_curso_sie = models.IntegerField(null=True, blank=True)
    sigla = models.CharField('Sigla do Programa', max_length=20, null=False, blank=True)
    nome_diploma = models.CharField('Nome do Programa', max_length=150, null=False, blank=True)
    nivel = models.CharField('Nível do programa', choices=niveis_programa, max_length=1, default='M')
    pagina_web = models.CharField('Endereço para a página do mestrado', null=True, blank=True, max_length=800)

    def __str__(self):
        return self.nome_diploma + ' : ' + self.nivel


class LinhaPesquisa(models.Model):
    programa = models.ForeignKey(Programa, verbose_name='programa', related_name='linhas_pesquisa',
                                 on_delete=models.CASCADE)
    descricao = models.CharField('Descrição', max_length=150)

    class Meta:
        verbose_name_plural = 'Linhas de pesquisa'

    def __str__(self):
        return self.descricao


class Arquivo(models.Model):

    def dir_arquivos(self, filename):
        extension = os.path.splitext(filename)[-1]
        return u'%s/%s/%s_%s%s' % ('arquivos_inscricao', self.ano, self.edicao, self.dataHora, extension)

    descricacao = models.CharField('Descrição do Arquivo', max_length=150, null=False, blank=True)
    arquivo = models.FileField(upload_to=dir_arquivos, storage=None, max_length=120, blank=True, null=True)


class ArquivoEtapa(models.Model):
    etapa = models.ForeignKey(Etapa, verbose_name='etapa', related_name='etapa_edital', on_delete=models.CASCADE)
    arquivo = models.ManyToManyField(Arquivo)


class Orientador(models.Model):
    nome = models.CharField('Nome do orientador', max_length=100)
    linhadepesquisa = models.ForeignKey(LinhaPesquisa, verbose_name='linha_depesquisa', related_name='orientador_set',
                                        on_delete=models.CASCADE)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name_plural = 'Orientadores'

    def __str__(self):
        return self.nome