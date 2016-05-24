from django.db import models


# Create your models here.
class Cliente(models.Model):
    """docstring for Cliente"""
    def __init__(self, *args, **kwargs):
        super(Cliente, self).__init__(*args, **kwargs)

    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=20,
                              default='activo',
                              blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]
