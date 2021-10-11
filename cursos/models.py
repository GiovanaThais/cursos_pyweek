from django.db import models

class Cursos(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    thumb = models.ImageField(upload_to = "thumb_cursos")

    def __str__(self) -> str:
        return self.nome
    class Meta:
        verbose_name = "Curso" 
        verbose_name_plural = "Cursos"

class Aulas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    aula = models.FileField(upload_to = "aulas")
    curso = models.ForeignKey(Cursos, on_delete = models.DO_NOTHING)


    def __str__(self) -> str:
        return self.nome
    class Meta:
        verbose_name = "Aula" 
        verbose_name_plural = "Aulas"
# Create your models here.
