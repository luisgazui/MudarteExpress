# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.TextField(blank=True)),
                ('telefono', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('estado', models.CharField(default='activo', blank=True, max_length=20)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
            },
        ),
    ]
