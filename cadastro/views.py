from django.shortcuts import render


# Create your views here.
def cadastrar_usuario(request):
    return render(request, 'cadastro/cadastrar_usuario.html')


def acessar(request):
    return render(request, 'cadastro/login.html')


def recuperar_senha(request):
    return render(request, 'cadastro/esqueci_senha.html')
