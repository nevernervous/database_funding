# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180331_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.CharField(default='Y', max_length=1, null=True),
        ),
    ]
