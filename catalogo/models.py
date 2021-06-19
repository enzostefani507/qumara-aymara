from django.db import models

class Producto(models.Model):
    nombre = models.CharField(
        max_length = 500,
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

    def __str__(self) -> str:
        return self.nombre