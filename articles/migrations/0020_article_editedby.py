# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20170805_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='editedby',
            field=models.CharField(default='luke', max_length=1000),
            preserve_default=False,
        ),
    ]
