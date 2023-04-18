from django.urls import path

from cadastro import views


urlpatterns = [
    path('', views.cadastrar_usuario, name='novo_usuario'),
    path('login/', views.acessar, name='acessar'),
    path('recuperar_senha/', views.recuperar_senha, name='recuperar_senha'),
]