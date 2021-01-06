from rest_framework import serializers
from .models import Contas

class ContaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contas
        fields = '__all__'
