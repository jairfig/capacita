from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from editais import views

urlpatterns = [
    path('', views.novo_edital, name='novo_edital'),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)