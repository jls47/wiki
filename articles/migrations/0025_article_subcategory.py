# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0024_auto_20170816_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subcategory',
            field=models.CharField(default='bees', max_length=100),
            preserve_default=False,
        ),
    ]