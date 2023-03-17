from django.shortcuts import render
from django.shortcuts import render


# Create your views here.
def novo_edital(request):
    return render(request, 'editais/novo_edital.html')


