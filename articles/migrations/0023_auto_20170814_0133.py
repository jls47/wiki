# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20170810_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categories',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
