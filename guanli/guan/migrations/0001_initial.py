# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ceng',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c', models.CharField(max_length=40, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])),
            ],
        ),
        migrations.CreateModel(
            name='guan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8f\xb7\xe7\xa0\x81')),
                ('jiage', models.IntegerField(verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('ceng', models.ForeignKey(verbose_name=b'\xe6\xa5\xbc\xe5\xb1\x82', to='guan.ceng')),
            ],
            options={
                'verbose_name': '\u9152\u5e97\u7ba1\u7406',
                'verbose_name_plural': '\u9152\u5e97\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='tex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, choices=[('\u5355\u4eba\u623f', '\u5355\u4eba\u623f'), ('\u666e\u901a\u5927\u5e8a\u623f', '\u666e\u901a\u5927\u5e8a\u623f'), ('\u8c6a\u534e\u5927\u5e8a\u623f', '\u8c6a\u534e\u5927\u5e8a\u623f'), ('\u5546\u52a1\u53cc\u5e8a\u623f', '\u5546\u52a1\u53cc\u5e8a\u623f')])),
            ],
        ),
        migrations.CreateModel(
            name='zhuangtai',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('z', models.CharField(max_length=40, choices=[('\u4f4f\u51c0', '\u4f4f\u51c0'), ('\u7a7a\u51c0', '\u7a7a\u51c0'), ('\u7a7a\u810f', '\u7a7a\u810f'), ('\u4f4f\u810f', '\u4f4f\u810f')])),
            ],
        ),
        migrations.AddField(
            model_name='guan',
            name='tex',
            field=models.ForeignKey(verbose_name=b'\xe6\x88\xbf\xe5\x9e\x8b', to='guan.tex'),
        ),
        migrations.AddField(
            model_name='guan',
            name='zhuangtai',
            field=models.ForeignKey(verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe7\x8a\xb6\xe6\x80\x81', to='guan.zhuangtai'),
        ),
    ]
