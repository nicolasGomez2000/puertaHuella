# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0002_auto_20180608_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('celular', models.CharField(max_length=20, blank=True)),
                ('mail', models.EmailField(max_length=30, blank=True)),
            ],
        ),
    ]
