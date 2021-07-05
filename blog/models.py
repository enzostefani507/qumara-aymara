from django.db import models
from django.utils import timezone

def fecha_actual():
    return timezone.now().strftime("%d/%m/%Y")

class Categoria(models.Model):
    nombre = models.CharField(
        max_length = 200,
        null = False,
        blank = False,
    )

class Post(models.Model):
    cateogoria = models.ForeignKey(Categoria)
    titulo = models.CharField(
        max_length = 100,
        help_text = "Ingrese el nombre del titulo",
        null = False,
        blank = False,
        editable = True
    )
    fecha_creacion = models.CharField(
        default=fecha_actual(),
        null = False,
        blank = False,
        editable = True
    )
    content = models.TextField()