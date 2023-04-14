from django.conf import settings
from django.db import models
from editais.models import Edital
from capacita import choices


# Create your models here.
class Candidato(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField('Nome completo', max_length=255)
    email = models.EmailField()
    celular = models.CharField('Telefone Celular', max_length=20, null=True, blank=True)
    whatsapp = models.BooleanField('Permite contactar por whatsapp', default=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    rg = models.CharField(max_length=20, null=True, blank=True)
    orgao_emissor = models.CharField(max_length=10, null=True, blank=True)
    data_emissao = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=choices.SEXO_CHOICES)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=60)
    estado = models.CharField(max_length=2, choices=choices.UF_CHOICES, default='AC')

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return f'{self.nome}/{self.estado}'


class Endereco(models.Model):
    logradouro = models.CharField('Rua', max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default='Rio Branco')
    cep = models.CharField(max_length=8)

    # vincular os campos cidade>estado no template.
    # https://gist.github.com/JhonatasMartins/7eed599a2f95d005b81f

    # cidade = models.CharField(max_length=255)
    # uf = models.CharField(max_length=2)
    # uf = forms.ChoiceField(widget=BRStateSelect(), initial='pr')

    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.bairro}. {self.cidade} - CEP: {self.cep}'


class Inscricao(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga_concorrencia = models.ForeignKey('editais.Vaga', on_delete=models.CASCADE, null=False, blank=False)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.candidato} inscrito no {self.vaga_concorrencia.edital.get_num_ano()} em {self.data} para a vaga {self.vaga_concorrencia}'

    class Meta:
        verbose_name_plural = 'Inscrições'