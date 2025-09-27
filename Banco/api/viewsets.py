from rest_framework import viewsets
from Banco.api import serializers

class MovimentacoesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Movimentacoeserializer
    queryset = serializers.models.Movimentacoes.objects.all()