from catalogo.models import Producto
from django.db import models
from django.utils import timezone

def fecha_actual():
    return timezone.now().strftime("%d/%m/%Y")

class Comentario(models.Model):
    nombre = models.CharField(
        max_length = 50,
        null = False,
        blank = False,
    )

    mensaje = models.CharField(
        max_length = 500,
        null = False,
        blank = False,
    )

    def __str__(self):
        return self.nombre + str(self.id)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length = 200,
        null = False,
        blank = False,
    )

    def __str__(self) -> str:
        return self.nombre

class Post(models.Model):
    imagen = models.CharField(
        max_length = 500,        
        editable = True
    )
    cateogoria = models.ForeignKey(
        Categoria,
        on_delete = models.RESTRICT,
    )
    descripcion = models.CharField(
        max_length = 100,
        help_text = "Indica una breve descripcion del tema",
        editable = True
    )
    titulo = models.CharField(
        max_length = 50,
        help_text = "Ingrese el nombre del titulo",
        null = False,
        blank = False,
        editable = True
    )
    
    fecha_creacion = models.CharField(
        default = fecha_actual(),
        max_length=50,
    )

    ingredientes = models.ManyToManyField(
        Producto, 
    )

    comentarios = models.ManyToManyField(
        Comentario,
    )

    content = models.TextField()



    def __str__(self):
        return self.titulo

    