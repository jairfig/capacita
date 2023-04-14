from django.shortcuts import render


# Create your views here.
def nova_incricao(request):
    return render(request, 'inscricoes/nova_inscricao.html')
