# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='celular',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='mail',
            field=models.EmailField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
