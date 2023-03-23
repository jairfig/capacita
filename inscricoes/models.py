from django.conf import settings
from django.db import models
from editais.models import Edital
from capacita import choices


# Create your models here.
class Candidato(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=20)
    orgao_emissor = models.CharField(max_length=10)
    data_emissao = models.DateField()
    sexo = models.CharField(max_length=1, choices=choices.SEXO_CHOICES)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=60)
    estado = models.CharField(max_length=2, choices=choices.UF_CHOICES, default='AC')

    def __unicode__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default='Rio Branco')
    cep = models.CharField(max_length=8)

    # vincular os campos cidade>estado no template.
    # https://gist.github.com/JhonatasMartins/7eed599a2f95d005b81f

    # cidade = models.CharField(max_length=255)
    # uf = models.CharField(max_length=2)
    # uf = forms.ChoiceField(widget=BRStateSelect(), initial='pr')

    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade} - {self.uf} - CEP: {self.cep}'


class Inscricao(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.candidato} inscrito no {self.edital} em {self.data}'
