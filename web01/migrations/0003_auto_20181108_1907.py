# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-08 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web01', '0002_auto_20181108_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='out_ip',
            field=models.GenericIPAddressField(),
        ),
    ]
