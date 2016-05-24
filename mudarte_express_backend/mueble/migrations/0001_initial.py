# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=7)),
                ('largo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('alto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('punto', models.IntegerField()),
                ('predefinido', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Muebles',
                'ordering': ['descripcion'],
                'verbose_name': 'Mueble',
            },
        ),
    ]
