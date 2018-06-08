# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0007_auto_20180608_1721'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Preceptoria',
        ),
        migrations.AddField(
            model_name='docente',
            name='categoria',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
