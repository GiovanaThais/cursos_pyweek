from django.contrib import admin
from .models import Cursos, Aulas, Comentarios, NotasAulas 

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao')

@admin.register(Aulas)
class AulasAdmin(admin.ModelAdmin):
    list_display = ('nome','curso','descricao')

@admin.register(NotasAulas)
class NotasAulasAdmin(admin.ModelAdmin):
    list_display = ('aula','nota','usuario')
admin.site.register(Comentarios)