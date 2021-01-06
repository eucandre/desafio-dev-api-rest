from rest_framework import generics
from .models import Transacoes
from .serializers import TransacaoSerializers
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from django_filters import rest_framework as filters
from rest_framework import viewsets


class TransacaoList(viewsets.ModelViewSet):
    queryset = Transacoes.objects.all()
    serializer_class = TransacaoSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

