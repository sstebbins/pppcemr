# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-30 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0143_auto_20160629_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_chart_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='is_telephone_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='is_waiting_room',
            field=models.BooleanField(default=False),
        ),
    ]
