from django.db import models
class Usuario(models.Model):
    nome = models.CharField("nome", max_length = 50)
    email = models.EmailField()
    senha = models.CharField("senha", max_length = 64)

    def __str__(self) -> str:
        return self.nome
    class Meta:
        verbose_name = "Usuario" 
        verbose_name_plural = "Usuarios"
# Create your models here.
