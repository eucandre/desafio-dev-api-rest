from rest_framework import serializers
from .models import Transacoes

class TransacaoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transacoes
        fields = '__all__'
