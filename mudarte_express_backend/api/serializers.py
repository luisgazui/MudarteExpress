from rest_framework import serializers
from django.contrib.auth.models import User
from cliente.models import Cliente
from mueble.models import Mueble
from contenedor.models import Contenedor
from bulto.models import Bulto
from cotizacionexpress.models import Cotizacion, CotizacionMueble, \
    CotizacionContenedor


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'is_staff', 'last_login',
                  'is_superuser', 'first_name',
                  'last_name', 'is_active',
                  'date_joined')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'direccion',
                  'telefono', 'email')


class MuebleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mueble
        fields = ('id', 'descripcion', 'ancho',
                  'largo', 'alto', 'punto',
                  'predefinido')


class ContenedorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contenedor
        fields = ('id', 'contenedor', 'siglas', 'unidad', 'punto')


class ContenedorDescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenedor
        fields = ('contenedor',)


class BultoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bulto
        fields = ('id', 'ancho', 'largo', 'alto', 'punto')


class CotizacionSerializer(serializers.HyperlinkedModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(many=False,
                                                 queryset=Cliente.objects.all())
    responsable = serializers.PrimaryKeyRelatedField(many=False,
                                                     queryset=User.objects.all())

    class Meta:
        model = Cotizacion
        fields = ('id', 'numero_cotizacion', 'cliente',
                  'responsable', 'fecha_de_cotizacion',
                  'total_cantidad', 'total_m3', 'estado')


class CotizacionMuebleSerializer(serializers.HyperlinkedModelSerializer):
    cotizacion = serializers.PrimaryKeyRelatedField(many=False,
                                                    queryset=Cotizacion.objects.all())

    class Meta:
        model = CotizacionMueble
        fields = ('id', 'cotizacion', 'mueble', 'descripcion',
                  'ancho', 'largo', 'alto', 'cantidad', 'punto',
                  'total_punto', 'estado')


class CotizacionContenedorSerializer(serializers.HyperlinkedModelSerializer):
    cotizacion = serializers.PrimaryKeyRelatedField(many=False,
                                                    queryset=Cotizacion.objects.all())

    class Meta:
        model = CotizacionContenedor
        fields = ('id', 'cotizacion', 'descripcion',
                  'cantidad', 'punto', 'estado')
