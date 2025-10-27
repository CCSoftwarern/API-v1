from rest_framework import serializers
from Banco import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Cria o usuário corretamente com senha criptografada
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class Movimentacoeserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movimentacoes
        fields = '__all__'

class CorrentistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Correntistas
        fields = '__all__'


class DepositoInSerializer(serializers.Serializer):
    """
    Serializer para validar os parâmetros de entrada da spDepositar.
    """
    correntista_id = serializers.IntegerField(
        required=True,
        min_value=1,
        help_text="O ID do correntista que receberá o depósito."
    )
    valor_deposito = serializers.DecimalField(
        max_digits=18,
        decimal_places=2,
        required=True,
        min_value=0.01,  # Não permite depósito de zero ou negativo
        help_text="O valor monetário a ser depositado."
    )

class PagarSerializer(serializers.Serializer):
    """
    Serializer para validar os parâmetros de entrada da spPagar.
    """
    correntista_id = serializers.IntegerField(
        required=True,
        min_value=1,
        help_text="O ID do correntista que realizará o pagamento."
    )
    valor_operacao = serializers.DecimalField(
        max_digits=18,
        decimal_places=2,
        required=True,
        min_value=0.01,  # Não permite pagamento de zero ou negativo
        help_text="O valor monetário a ser pago."
    )
    descricao = serializers.CharField(
        max_length=50,
        help_text="Descrição do pagamento."
    )
 

class TransferirSerializer(serializers.Serializer):
    correntista_id = serializers.IntegerField(
        required=True,
        min_value=1,
        help_text="O ID do correntista que realizará a transferência."
    )
    valor_operacao = serializers.DecimalField(
        max_digits=18,
        decimal_places=2,
        required=True,
        min_value=0.01,  # Não permite transferência de zero ou negativo
        help_text="O valor monetário a ser transferido."
    )
    CorrentistaBeneficiari_id = serializers.IntegerField(
        required=True,
        min_value=1,
        help_text="O ID do correntista beneficiário da transferência."
    )

class SacarSerializer(serializers.Serializer):
    """
    Serializer para validar os parâmetros de entrada da spSacar.
    """
    correntista_id = serializers.IntegerField(
        required=True,
        min_value=1,
        help_text="O ID do correntista que realizará o saque."
    )
    valor_saque = serializers.DecimalField(
        max_digits=18,
        decimal_places=2,
        required=True,
        min_value=0.01,  # Não permite saque de zero ou negativo
        help_text="O valor monetário a ser sacado."
    )