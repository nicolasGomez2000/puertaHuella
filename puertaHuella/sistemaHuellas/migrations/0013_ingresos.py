# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0012_delete_asistencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ingresos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
    ]
