# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField(max_length=600)),
                ('toc', models.CharField(max_length=600)),
                ('body', models.TextField(max_length=10000000)),
                ('categories', models.CharField(max_length=600)),
                ('featured', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(max_length=600)),
                ('edited', models.CharField(max_length=600)),
                ('created', models.CharField(max_length=600)),
            ],
        ),
    ]
