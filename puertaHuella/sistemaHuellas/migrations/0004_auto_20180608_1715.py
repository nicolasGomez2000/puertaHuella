# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0003_docente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreCurso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreMateria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Preceptoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('celular', models.CharField(max_length=20, blank=True)),
                ('mail', models.EmailField(max_length=30, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
