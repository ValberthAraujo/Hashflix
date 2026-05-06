from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANÁLISE","Análise"),
    ("CURSOS LIXO", "Cursos Lixo"),
    ("CURSOS TOPS", "Cursos Tops")
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    thumb = models.ImageField(upload_to='thumbs/')
    categoria = models.CharField(max_length=100, choices=LISTA_CATEGORIAS)
    datalancamento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo