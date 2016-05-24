from django.db import models


# Create your models here.
class Mueble(models.Model):
    """docstring for Mueble"""
    def __init__(self, *args, **kwargs):
        super(Mueble, self).__init__(*args, **kwargs)

    descripcion = models.CharField(max_length=100, unique=True)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    punto = models.IntegerField()
    predefinido = models.BooleanField(default=None)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Mueble"
        verbose_name_plural = "Muebles"
        ordering = ["descripcion"]
