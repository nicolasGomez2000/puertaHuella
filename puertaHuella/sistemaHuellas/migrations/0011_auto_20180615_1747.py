# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0010_alumno_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('fechaNac', models.DateField()),
                ('celular', models.CharField(max_length=20, blank=True)),
                ('mail', models.EmailField(max_length=30, blank=True)),
                ('imagen', models.ImageField(default=None, null=True, upload_to=b'images')),
            ],
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='fechaNac',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='id',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='nombre',
        ),
        migrations.AddField(
            model_name='docente',
            name='imagen',
            field=models.ImageField(default=None, null=True, upload_to=b'images'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='persona_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='sistemaHuellas.Persona'),
            preserve_default=False,
        ),
    ]
