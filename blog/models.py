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
    imagen = models.CharField(
        max_length = 500,
        null = False,
        blank = False,
        editable = True
    )
    cateogoria = models.ForeignKey(
        Categoria,
        on_delete = models.RESTRICT,
    )
    descripcion = models.CharField(
        max_length = 100,
        help_text = "Indica una breve descripcion del tema",
        null = False,
        blank = False,
        editable = True
    )
    titulo = models.CharField(
        max_length = 50,
        help_text = "Ingrese el nombre del titulo",
        null = False,
        blank = False,
        editable = True
    )
    fecha_creacion = models.DateField(
        default=fecha_actual(),
        null = False,
        blank = False,
        editable = True,
    )
    content = models.TextField()