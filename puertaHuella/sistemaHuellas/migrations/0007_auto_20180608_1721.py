# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0006_auto_20180608_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='fechaNacimiento',
            new_name='fechaNac',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='nombreCurso',
            new_name='nomCurso',
        ),
        migrations.RenameField(
            model_name='docente',
            old_name='fechaNacimiento',
            new_name='fechaNac',
        ),
        migrations.RenameField(
            model_name='materia',
            old_name='nombreMateria',
            new_name='nomMateria',
        ),
        migrations.RenameField(
            model_name='preceptoria',
            old_name='fechaNacimiento',
            new_name='fechaNac',
        ),
    ]
