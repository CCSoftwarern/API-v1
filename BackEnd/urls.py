
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Banco.api import viewsets as banco_viewsets
from Banco.views import CustomAuthToken

route = routers.DefaultRouter()
route.register(r'movimentacoes', banco_viewsets.MovimentacoesViewSet, basename='Movimentacoes')
route.register(r'depositos', banco_viewsets.DepositarViewSet, basename='deposito')
route.register(r'pagamentos', banco_viewsets.PagarViewSet, basename='pagamento')
route.register(r'transferencias', banco_viewsets.TransferirViewSet, basename='transferencia')
route.register(r'saques', banco_viewsets.SacarViewSet, basename='saque')
route.register(r'extratos', banco_viewsets.ExtratoViewSet, basename='extrato')
route.register(r'correntistas', banco_viewsets.CorrentistasViewSet, basename='Correntistas')
route.register(r'users', banco_viewsets.UserViewSet, basename='User')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/', include(route.urls)),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),
]
