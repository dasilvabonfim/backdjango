from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.


class ReactView(APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        output = [{'nome': output.nome, 'preco': output.preco, 'descricao': output.descricao, 'imagem': output.imagem}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class UsuarioView(APIView):

    serializer_class = NewModelSerializer

    def get(self, request):
        output = [{'nome': output.nome, 'email': output.email, 'senha': output.senha}
                  for output in Usuario.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = NewModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)