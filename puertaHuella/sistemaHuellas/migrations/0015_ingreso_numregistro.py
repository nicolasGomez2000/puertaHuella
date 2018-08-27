# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaHuellas', '0014_auto_20180827_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='numRegistro',
            field=models.IntegerField(default=datetime.datetime(2018, 8, 27, 17, 15, 28, 31000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
