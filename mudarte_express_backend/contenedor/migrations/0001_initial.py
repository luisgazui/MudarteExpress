# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('contenedor', models.CharField(unique=True, max_length=100)),
                ('siglas', models.CharField(max_length=10)),
                ('unidad', models.IntegerField()),
                ('punto', models.IntegerField()),
            ],
            options={
                'ordering': ['contenedor'],
                'verbose_name_plural': 'Contenedores',
                'verbose_name': 'Contenedor',
            },
        ),
    ]
