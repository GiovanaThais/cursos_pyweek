from rest_framework import generics
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from usuarios import models
from .serializers import UsuarioSerializer
from django.shortcuts import get_object_or_404


class ListarUsuarioAPIView(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = models.Usuario.objects.all()
    

class UsuarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = models.Usuario.objects.all()
    