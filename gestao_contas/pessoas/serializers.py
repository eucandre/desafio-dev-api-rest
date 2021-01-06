from rest_framework import serializers
from .models import Pessoas

class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = '__all__'
