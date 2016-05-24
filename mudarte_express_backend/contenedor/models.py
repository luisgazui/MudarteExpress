from django.db import models


# Create your models here.
class Contenedor(models.Model):
    """docstring for Contenedor"""
    def __init__(self, *args, **kwargs):
        super(Contenedor, self).__init__(*args, **kwargs)

    contenedor = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    unidad = models.IntegerField()
    punto = models.IntegerField()

    def __str__(self):
        return self.contenedor

    class Meta:
        verbose_name = "Contenedor"
        verbose_name_plural = "Contenedores"
        ordering = ["contenedor"]
