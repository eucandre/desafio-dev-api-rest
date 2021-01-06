from rest_framework import serializers
from .models import Transacoes

class TransacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transacoes
        fields = '__all__'
