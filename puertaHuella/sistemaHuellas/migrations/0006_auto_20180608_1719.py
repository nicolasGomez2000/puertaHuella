# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0005_auto_20180608_1717'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cursos',
            new_name='Curso',
        ),
        migrations.RenameModel(
            old_name='Preceptor',
            new_name='Preceptoria',
        ),
    ]
