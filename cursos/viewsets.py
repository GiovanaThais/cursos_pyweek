from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication 
from rest_framework import filters
from rest_framework.filters import SearchFilter

from cursos import serializers
from rest_framework import generics
#from rest_framework.generics import generics
from .serializers import CursosSerializer, AulasSerializer, ComentariosSerializer

from cursos import models



class ListarCursosAPIView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated, )
    #authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'email'] #filtro de pesquisa

    serializer_class = CursosSerializer
    queryset = models.Cursos.objects.all()

class CursosAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cursos.objects.all()
    serializer_class = CursosSerializer

class ListarAulasAPIView(generics.ListCreateAPIView):
    queryset = models.Aulas.objects.all()
    serializer_class = AulasSerializer

    def get_queryset(self):
        if self.kwargs.get('aula_pk'):
            return self.queryset.filter(aula_id=self.kwargs.get('aula_pk'))
        return self.queryset.all()

class AulasAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AulasSerializer
    queryset = models.Aulas.objects.all()

