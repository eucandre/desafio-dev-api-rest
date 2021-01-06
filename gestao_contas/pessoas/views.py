from .models import Pessoas
from .serializers import PessoaSerializers
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from django_filters import rest_framework as filters
from rest_framework import viewsets


class PessoasList(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoaSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

