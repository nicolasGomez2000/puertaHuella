# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0009_asistencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='imagen',
            field=models.ImageField(default=None, null=True, upload_to=b'images'),
        ),
    ]
