from django.db import models

class Producto(models.Model):
    marca = models.CharField(
        max_length = 50,
        null = False,
        blank = True,
        editable = True,
    )
    nombre = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        editable=True,
    )
    imagen = models.CharField(
        max_length = 500,
        null = False,
        blank = False,
        editable = True
    )
    en_stock_actual = models.BooleanField(
        default = False,
        null = False,
        blank = False,
        editable = True
    )
    comentario = models.CharField(
        max_length = 500,
        null = False,
        blank = True,
    )
    def __str__(self) -> str:
        return self.nombre