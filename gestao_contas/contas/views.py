from rest_framework import generics
from .models import Contas
from .serializers import ContaSerializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django_filters import rest_framework as filters
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'contas': reverse('contas-list', request=request, format=format)
    })

class ContasList(generics.ListCreateAPIView):
    queryset = Contas.objects.all()
    serializer_class = ContaSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)