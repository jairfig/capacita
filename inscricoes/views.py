from django.shortcuts import render


# Create your views here.
def novo_edital(request):
    return render(request, 'inscricoes/nova_inscricao.html')
