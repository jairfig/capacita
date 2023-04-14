from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from inscricoes import views

urlpatterns = [
    path('', views.nova_incricao, name='nova_inscricao'),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)