# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-26 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0139_auto_20160626_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='is_billed',
            field=models.BooleanField(default=True),
        ),
    ]