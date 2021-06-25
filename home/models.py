from django.db import models
from django.utils import timezone

def fecha_actual():
    return timezone.now().strftime("%d/%m/%Y")

class Opinion(models.Model):
    autor = models.CharField(
        max_length = 500,
        null = False,
        blank = False,
        editable=True,
    )
    contenido = models.CharField(
        max_length = 500,
        null = False,
        blank = False,
        editable = True
    )

    fecha_creacion = models.CharField(
        max_length=50,
        default=fecha_actual()
    )

    def __str__(self):
        return self.autor + "-" + str(self.id)