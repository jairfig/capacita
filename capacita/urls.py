"""capacita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from painel import views

urlpatterns = [
    path('painel/', views.painel, name='painel'),
    path('editais/', include('editais.urls')),
    path('inscricoes/', include('inscricoes.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('cadastro/', include('django.contrib.auth.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
