# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20170802_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='user', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='pastFeatured',
            field=models.BooleanField(default=False),
        ),
    ]
