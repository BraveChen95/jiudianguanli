# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ceng',
            old_name='c',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='zhuangtai',
            old_name='z',
            new_name='name',
        ),
    ]
