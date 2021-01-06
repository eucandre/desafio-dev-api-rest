from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PessoasList.as_view(), name='pessoas-list'),
]