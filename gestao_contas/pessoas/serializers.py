from rest_framework import serializers
from .models import Pessoas

class PessoaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoas
        fields = '__all__'
