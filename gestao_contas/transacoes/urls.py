from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TransacaoList.as_view(), name='transacoes-list'),
]