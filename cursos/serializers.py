
from rest_framework import serializers
from .models import Cursos, Aulas, Comentarios, NotasAulas


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