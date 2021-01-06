from django.urls import path, include
from . import views

urlpatterns = [
    path('contas/', views.ContaList.as_view()),
    path('contas/<int:pk>/', views.ContaDetalhes.as_view()),
]