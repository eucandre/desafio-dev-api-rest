from django.http import HttpResponse
from requests import Response
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Contas
from .serializers import ContaSerializers

class ContaList(generics.ListCreateAPIView):
    queryset = Contas.objects.all()
    serializer_class = ContaSerializers

class ContaDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contas.objects.all()
    serializer_class = ContaSerializers
