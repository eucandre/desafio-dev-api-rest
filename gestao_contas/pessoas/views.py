from rest_framework import generics
from .models import Pessoas
from .serializers import PessoaSerializers


class PessoasList(generics.ListCreateAPIView):
    queryset = Pessoas.objects.all()
    serializer_class = PessoaSerializers
