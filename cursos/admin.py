from django.contrib import admin
from .models import Cursos, Aulas 

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao')

@admin.register(Aulas)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','curso','descricao')

