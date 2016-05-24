from django.contrib.auth.models import User
from rest_framework import viewsets
from cliente.models import Cliente
from mueble.models import Mueble
from contenedor.models import Contenedor
from cotizacionexpress.models import Cotizacion, CotizacionMueble, \
    CotizacionContenedor
from bulto.models import Bulto
from api.serializers import UserSerializer, ClienteSerializer, \
    MuebleSerializer, ContenedorSerializer, CotizacionSerializer, \
    CotizacionMuebleSerializer, CotizacionContenedorSerializer, \
    ContenedorDescripcionSerializer, BultoSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class MuebleViewSet(viewsets.ModelViewSet):
    queryset = Mueble.objects.all()
    serializer_class = MuebleSerializer


class ContenedorViewSet(viewsets.ModelViewSet):
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'contenedor' in query.keys():
            queryset = queryset.filter(contenedor=query.get('contenedor')).order_by('-unidad')

        return queryset


class ContenedorDescripcionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contenedor.objects.values('contenedor').distinct()
    serializer_class = ContenedorDescripcionSerializer


class BultoViewSet(viewsets.ModelViewSet):
    queryset = Bulto.objects.all()
    serializer_class = BultoSerializer


class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer


class CotizacionMuebleViewSet(viewsets.ModelViewSet):
    queryset = CotizacionMueble.objects.all()
    serializer_class = CotizacionMuebleSerializer
    lookup_field = 'id'

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'cotizacion' in query.keys():
            queryset = queryset.filter(cotizacion=Cotizacion.objects.get(id=query.get('cotizacion')))

        return queryset


class CotizacionContenedorViewSet(viewsets.ModelViewSet):
    queryset = CotizacionContenedor.objects.all()
    serializer_class = CotizacionContenedorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'cotizacion' in query.keys():
            queryset = queryset.filter(cotizacion=Cotizacion.objects.get(id=query.get('cotizacion')))

        return queryset
