from django.db import models
from django.core.validators import MinValueValidator

class Mercancia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=250, blank=True)  # Permite descripciones vacías
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    qr_number = models.CharField(max_length=50, unique=True)  # Cambiado a CharField para mayor flexibilidad
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Mercancía'
        verbose_name_plural = 'Mercancías'