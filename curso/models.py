from mailbox import NotEmptyError
from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=600)

    def __str__(self):
        return self.nome