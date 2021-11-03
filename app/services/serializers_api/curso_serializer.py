from rest_framework import serializers
from cursos.models import Cursos, Aulas, Comentarios, NotasAulas

#class CursosServices(CursosServicer):
class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields ='__all__'
        
class AulasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aulas
        fields ='__all__'

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields ='__all__'
class NotasAulasSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotasAulas
        fields ='__all__'
        