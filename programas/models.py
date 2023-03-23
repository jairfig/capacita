from django.db import models
from capacita import choices


# Create your models here.
class Programa(models.Model):
    cod_curso_sie = models.IntegerField(null=True, blank=True)
    sigla = models.CharField('Sigla do Programa', max_length=20, null=False, blank=True)
    nome_diploma = models.CharField('Nome do Programa', max_length=150, null=False, blank=True)
    nivel = models.CharField('Nível do programa', choices=choices.NIVEL_PROGRAMA_CHOICE, max_length=1, default='M')
    pagina_web = models.CharField('Endereço para a página do mestrado', null=True, blank=True, max_length=800)

    def __str__(self):
        return self.nome_diploma + ' : ' + self.nivel


class LinhaPesquisa(models.Model):
    programa = models.ForeignKey(Programa, verbose_name='Programa', related_name='linhas_pesquisa',
                                 on_delete=models.CASCADE)
    descricao = models.CharField('Nome da Linha de Pesquisa', max_length=150)
    sigla = models.CharField('Sigla da área', max_length=12, null=True, blank=True)

    def __str__(self):
        return self.descricao

    def get_programa(self):
        return self.programa

    def get_nivel_programa(self):
        return self.programa.get_nivel_display()

    class Meta:
        verbose_name_plural = 'Linhas de pesquisa'


class AreaTrabalho(models.Model):
    linha_pesquisa = models.ForeignKey(LinhaPesquisa, verbose_name='Linha', related_name='areas_trabalho',
                                 on_delete=models.CASCADE)
    area = models.CharField('Título da Área', max_length=150)

    def __str__(self):
        return f'{self.area} ({self.linha_pesquisa.sigla})'

    class Meta:
        ordering = ["area"]
        verbose_name_plural = u'Areas de Trabalho'


class Orientador(models.Model):
    nome = models.CharField('Nome do orientador', max_length=100)
    area = models.ForeignKey(AreaTrabalho, verbose_name='Área de Pesquisa', related_name='orientadores',
                                        on_delete=models.CASCADE, null=True, blank=True)
    linha = models.ForeignKey(LinhaPesquisa, verbose_name='Linha de Pesquisa', related_name='orientadores',
                                        on_delete=models.CASCADE, null=True, blank=True)
    ativo = models.BooleanField('Ativo', default=True)

    def get_linha_pesquisa(self):
        return self.linha or self.area.linha_pesquisa

    def get_programa(self):
        return self.area.linha_pesquisa.programa or self.linha.programa

    class Meta:
        verbose_name_plural = 'Orientadores'

    def __str__(self):
        return self.nome
