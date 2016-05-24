from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente


ESTADO_CHOICES = (
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    )


# Create your models here.
class Cotizacion(models.Model):
    """docstring for Cotización"""
    def __init__(self, *args, **kwargs):
        super(Cotizacion, self).__init__(*args, **kwargs)

    numero_cotizacion = models.CharField(max_length=100, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    responsable = models.ForeignKey(User, null=True, blank=True)
    fecha_de_cotizacion = models.DateTimeField(auto_now_add=True, blank=True)
    total_cantidad = models.IntegerField(blank=True, default=0)
    total_m3 = models.DecimalField(max_digits=7, decimal_places=2,
                                   blank=True, default=0.00)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"


class CotizacionMueble(models.Model):
    """docstring for CotizacionMueble"""
    def __init__(self, *args, **kwargs):
        super(CotizacionMueble, self).__init__(*args, **kwargs)

    cotizacion = models.ForeignKey(Cotizacion)
    mueble = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    ancho = models.DecimalField(max_digits=7, decimal_places=2)
    largo = models.DecimalField(max_digits=7, decimal_places=2)
    alto = models.DecimalField(max_digits=7, decimal_places=2)
    cantidad = models.IntegerField()
    punto = models.IntegerField()
    total_punto = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return str(self.mueble)

    class Meta:
        verbose_name = "mueble de la cotización"
        verbose_name_plural = "Muebles de la cotización"
        ordering = ["mueble"]


class CotizacionContenedor(models.Model):
    """docstring for Cotización"""
    def __init__(self, *args, **kwargs):
        super(CotizacionContenedor, self).__init__(*args, **kwargs)

    cotizacion = models.ForeignKey(Cotizacion)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    punto = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return str(self.descripcion)

    class Meta:
        verbose_name = "Contenedor de la cotización"
        verbose_name_plural = "Contenedores de la cotización"
        ordering = ["descripcion"]
