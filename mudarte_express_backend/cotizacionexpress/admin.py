from django.contrib import admin
from cotizacionexpress.models import Cotizacion, CotizacionMueble, CotizacionContenedor


# Register your models here.
admin.site.register(Cotizacion)
admin.site.register(CotizacionMueble)
admin.site.register(CotizacionContenedor)
