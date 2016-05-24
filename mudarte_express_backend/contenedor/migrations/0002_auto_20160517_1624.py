# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenedor',
            name='contenedor',
            field=models.CharField(max_length=100),
        ),
    ]
