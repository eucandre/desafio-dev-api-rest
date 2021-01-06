from rest_framework import generics
from .models import Transacoes
from .serializers import TransacaoSerializers


class TransacaoList(generics.ListCreateAPIView):
    queryset = Transacoes.objects.all()
    serializer_class = TransacaoSerializers
