# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacionexpress', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacioncontenedor',
            name='total_punto',
        ),
        migrations.AddField(
            model_name='cotizacionmueble',
            name='total_punto',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='estado',
            field=models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')]),
        ),
        migrations.AlterField(
            model_name='cotizacioncontenedor',
            name='estado',
            field=models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')]),
        ),
        migrations.AlterField(
            model_name='cotizacionmueble',
            name='estado',
            field=models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')]),
        ),
    ]
