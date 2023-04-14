# _*_coding:utf-8_*_
from datetime import datetime

from django.core.exceptions import ValidationError
def validate_extension(filename, valid_extensions=['PDF', 'DOC']):
    """
    Validate an extension
    :param filename:
    :param valid_extensions:
    :return:

    Usage:
    validate_extension('filename.txt', ['PDF', 'TXT', 'DOC', 'DOCX'])
    """
    ext = filename.split('.')[-1].upper()
    if ext in valid_extensions:
        return True
    raise ValidationError('Extensões permitidas: %s' % ''.join(valid_extensions))

def validate_file_extension_pdf(value):
    if not value.name.endswith('.pdf') and not value.name.endswith('.PDF'):
        raise ValidationError('Arquivo permitido somente em formato ".pdf"')

def validate_file_extension_img(value):
    if not value.name.endswith('.JPG') and not value.name.endswith('.jpg') \
            and not value.name.endswith('.JPEG') and not value.name.endswith('.jpeg'):
        raise ValidationError('Arquivo permitido somente em formato JPG ou JPEG')


def validate_file_extension_doc(value):
    if not value.name.endswith('.doc') and not value.name.endswith('.DOC') \
            and not value.name.endswith('.docx') and not value.name.endswith('.DOCX') \
            and not value.name.endswith('.odt') and not value.name.endswith('.ODT'):
        raise ValidationError('Arquivo permitido somente em formato "pdf, doc, docx ou odt"')


def data_valida(value):
    if value < datetime(1900, 1, 1).date():
        raise ValidationError('Informe uma data válida.')


#Utilizado para retornar um dígito verificador de CPF
def dv(cpf, inicio, fim):
    soma = 0
    for i in range(inicio, fim):
        soma += int(cpf[i])*(fim+1-i)
    resto = soma%11
    if resto < 2:
        return 0
    else:
        return 11 - resto

#Utilizado para retornar o primeiro dígito verificador de CPF
def dv1(cpf):
    return dv(cpf, 0, 9)

#Utilizado para retornar o segundo dígito verificador de CPF
def dv2(cpf):
    return dv(cpf, 0, 10)


def formatar_cpf(cpf):

    cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11:
        return False

    c = cpf[0]
    dif = False
    for i in range(0, 11):
        try:
            int(cpf[i])
        except:
            return False
        if c!= cpf[i]:
            dif = True
        c = cpf[i]
    if not dif:
        return False
    if int(cpf[9]) == dv1(cpf) and int(cpf[10]) == dv2(cpf):
        return '%s.%s.%s-%s' % (cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    else:
        return False