# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20170726_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussions', models.TextField(max_length=9999999999999999999)),
            ],
        ),
    ]