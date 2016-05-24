# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('numero_cotizacion', models.CharField(blank=True, max_length=100)),
                ('fecha_de_cotizacion', models.DateTimeField(auto_now_add=True)),
                ('total_puntos', models.IntegerField(default=0, blank=True)),
                ('total_m3', models.DecimalField(default=0.0, max_digits=7, blank=True, decimal_places=2)),
                ('estado', models.CharField(default='activo', blank=True, max_length=20)),
                ('cliente', models.ForeignKey(blank=True, to='cliente.Cliente', null=True)),
                ('responsable', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cotizaciones',
                'verbose_name': 'Cotización',
            },
        ),
        migrations.CreateModel(
            name='CotizacionContenedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('punto', models.IntegerField()),
                ('total_punto', models.IntegerField()),
                ('estado', models.CharField(default='activo', blank=True, max_length=20)),
                ('cotizacion', models.ForeignKey(to='cotizacionexpress.Cotizacion')),
            ],
            options={
                'ordering': ['descripcion'],
                'verbose_name_plural': 'Contenedores de la cotización',
                'verbose_name': 'Contenedor de la cotización',
            },
        ),
        migrations.CreateModel(
            name='CotizacionMueble',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('mueble', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('ancho', models.DecimalField(max_digits=7, decimal_places=2)),
                ('largo', models.DecimalField(max_digits=7, decimal_places=2)),
                ('alto', models.DecimalField(max_digits=7, decimal_places=2)),
                ('cantidad', models.IntegerField()),
                ('punto', models.IntegerField()),
                ('estado', models.CharField(default='activo', blank=True, max_length=20)),
                ('cotizacion', models.ForeignKey(to='cotizacionexpress.Cotizacion')),
            ],
            options={
                'ordering': ['mueble'],
                'verbose_name_plural': 'Muebles de la cotización',
                'verbose_name': 'mueble de la cotización',
            },
        ),
    ]
