from rest_framework import serializers
from Banco import models

class Movimentacoeserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movimentacoes
        fields = '__all__'