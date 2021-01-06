from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('/contas-lista/', views.ContasList.as_view(), name='contas-list'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.api_root),
]