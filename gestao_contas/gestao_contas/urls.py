from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('contas',include('contas.urls')),
    path('pessoas',include('pessoas.urls')),
    path('transacoes',include('transacoes.urls')),
    path('admin/', admin.site.urls),
]
