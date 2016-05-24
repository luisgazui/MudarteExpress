from django.db import models


# Create your models here.
class Bulto(models.Model):
    """docstring for Bulto"""
    def __init__(self, *args, **kwargs):
        super(Bulto, self).__init__(*args, **kwargs)

    ancho = models.IntegerField()
    largo = models.IntegerField()
    alto = models.IntegerField()
    punto = models.IntegerField()

    def __str__(self):

        return u' %s x %s x %s' % (self.ancho, self.largo, self.alto)

    class Meta:
        verbose_name = "Bulto"
        verbose_name_plural = "Bultos"
