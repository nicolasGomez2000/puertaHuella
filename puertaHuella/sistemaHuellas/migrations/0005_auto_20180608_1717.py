# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0004_auto_20180608_1715'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preceptoria',
            new_name='Preceptor',
        ),
    ]
