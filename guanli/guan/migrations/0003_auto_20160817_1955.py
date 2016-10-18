# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guan', '0002_auto_20160816_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guan',
            name='num',
            field=models.IntegerField(unique=True, verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8f\xb7\xe7\xa0\x81'),
        ),
    ]
