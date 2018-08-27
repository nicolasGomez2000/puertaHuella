# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0013_ingresos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ingresos',
            new_name='ingreso',
        ),
    ]
