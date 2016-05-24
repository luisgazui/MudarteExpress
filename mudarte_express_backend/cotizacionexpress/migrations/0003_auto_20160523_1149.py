# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacionexpress', '0002_auto_20160518_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cotizacion',
            old_name='total_puntos',
            new_name='total_cantidad',
        ),
    ]
