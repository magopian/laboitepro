# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-14 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boites', '0005_auto_20161013_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boite',
            name='api_key',
            field=models.CharField(default=b'e3cbaff7', max_length=8, verbose_name="Cl\xe9 d'API"),
        ),
    ]
