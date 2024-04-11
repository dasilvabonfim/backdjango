from rest_framework import serializers
from .models import React, Usuario
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['nome', 'preco', 'descricao','imagem']

class NewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'telefone']