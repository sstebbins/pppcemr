# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 17:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0117_auto_20160322_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='treatment_option',
        ),
    ]
