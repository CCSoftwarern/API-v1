from rest_framework import viewsets
from Banco.api import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from Banco.services import executar_sp_depositar, executar_sp_pagar, executar_sp_sacar, executar_sp_transferir, executar_vw_extrato 
from .serializers import DepositoInSerializer, PagarSerializer, SacarSerializer, TransferirSerializer # Importa o Serializer de Input

class MovimentacoesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Movimentacoeserializer
    queryset = serializers.models.Movimentacoes.objects.all()

class ExtratoViewSet(viewsets.GenericViewSet):
    @action(detail=True, methods=['get'])
    def extrato(self, request, pk=None):
        try:
            movimentacoes = executar_vw_extrato(pk)
            return Response(movimentacoes, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"detail": f"Erro ao recuperar extrato: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DepositarViewSet(viewsets.GenericViewSet):
    serializer_class = DepositoInSerializer 
    @action(detail=False, methods=['post'])
    def depositar(self, request):
        input_serializer = DepositoInSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        
        # Dados validados
        validated_data = input_serializer.validated_data
        
        correntista_id = validated_data['correntista_id']
        valor_deposito = validated_data['valor_deposito']
        
        # 2. EXECUÇÃO da Stored Procedure
        try:
            executar_sp_depositar(correntista_id, valor_deposito)
            
            # 3. Retorno de Sucesso (200 OK ou 201 Created)
            return Response({
                "mensagem": "Depósito realizado com sucesso.",
                "correntista_id": correntista_id,
                "valor_depositado": valor_deposito
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
            # Captura o erro relançado pelo service.py
            return Response(
                {"detail": f"Falha na transação: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class PagarViewSet(viewsets.GenericViewSet):
    serializer_class = PagarSerializer 
    @action(detail=False, methods=['post'])
    def pagar(self, request):
        input_serializer = PagarSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data
        
        correntista_id = validated_data['correntista_id']
        valor_operacao = validated_data['valor_operacao']
        descricao = validated_data['descricao']
        
        try:
            executar_sp_pagar(correntista_id, valor_operacao, descricao)
   
            return Response({
                "mensagem": "Pagamento realizado com sucesso.",
                "correntista_id": correntista_id,
                "valor_depositado": valor_operacao,
                "descricao": descricao
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
        
            return Response(
                {"detail": f"Falha na transação: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        
class TransferirViewSet(viewsets.GenericViewSet):
    serializer_class = TransferirSerializer 
    @action(detail=False, methods=['post'])
    def transferir(self, request):
        input_serializer = TransferirSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data
        
        correntista_id = validated_data['correntista_id']
        valor_operacao = validated_data['valor_operacao']
        CorrentistaBeneficiari_id = validated_data['CorrentistaBeneficiari_id']
        
        try:
            executar_sp_transferir(correntista_id, valor_operacao, CorrentistaBeneficiari_id)
   
            return Response({
                "mensagem": "Transferência realizada com sucesso.",
                "correntista_id": correntista_id,
                "valor_operacao": valor_operacao,
                "CorrentistaBeneficiari_id": CorrentistaBeneficiari_id
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
        
            return Response(
                {"detail": f"Falha na transação: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR 
            ) 

class SacarViewSet(viewsets.GenericViewSet):
    serializer_class = SacarSerializer 
    @action(detail=False, methods=['post'])
    def sacar(self, request):
        input_serializer = SacarSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data
        
        correntista_id = validated_data['correntista_id']
        valor_saque = validated_data['valor_saque']
        
        try:
            executar_sp_sacar(correntista_id, valor_saque)
   
            return Response({
                "mensagem": "Saque realizado com sucesso.",
                "correntista_id": correntista_id,
                "valor_saque": valor_saque
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
        
            return Response(
                {"detail": f"Falha na transação: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)  