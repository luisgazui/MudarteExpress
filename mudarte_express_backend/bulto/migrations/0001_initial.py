# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ancho', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('alto', models.IntegerField()),
                ('punto', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Bulto',
                'verbose_name_plural': 'Bultos',
            },
        ),
    ]
