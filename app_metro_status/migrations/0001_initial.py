# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-17 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boites', '0008_auto_20161017_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppMetroStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='Indique si cette app est activ\xe9e sur votre bo\xeete', verbose_name='App activ\xe9e ?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='Derni\xe8re activit\xe9')),
                ('failures', models.TextField(verbose_name='Pannes')),
                ('boite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boites.Boite', verbose_name='Bo\xeete')),
            ],
            options={
                'verbose_name': 'Configuration : statut lignes de m\xe9tro',
                'verbose_name_plural': 'Configurations : statut lignes de m\xe9tro',
            },
        ),
    ]