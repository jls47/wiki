# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 06:53
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=ckeditor.fields.RichTextField(verbose_name='Summary'),
        ),
    ]