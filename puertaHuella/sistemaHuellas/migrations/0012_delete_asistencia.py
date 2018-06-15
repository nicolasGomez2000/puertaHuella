# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0011_auto_20180615_1747'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Asistencia',
        ),
    ]
