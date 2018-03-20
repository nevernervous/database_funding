# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor', models.TextField()),
                ('title', models.TextField()),
                ('link', models.CharField(max_length=300)),
                ('amount', models.IntegerField()),
                ('deadline', models.DateField(blank=True, null=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('active', models.CharField(default='Y', max_length=1)),
            ],
        ),
    ]
