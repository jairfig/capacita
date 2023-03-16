from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def painel(request):
    context = {
        'local': "painel",
    }
    return render(request, 'painel/painel.html', context)


def dashboard(request):
    return render(request, 'painel/dashboard.html')
