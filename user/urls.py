from django.urls import path
from user.views import cadastro_usuario, confirmacao_cadastro

urlpatterns = [
    path('', cadastro_usuario, name='cadastro_usuario'),
    path('confirmacao', confirmacao_cadastro, name='confirmacao_cadastro'),


]
