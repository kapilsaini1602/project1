# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-17 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepg', '0002_auto_20211117_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insert',
            name='Designation',
            field=models.CharField(error_messages={b'unique': b'This email has already been registered.'}, max_length=30, unique=True),
        ),
    ]
