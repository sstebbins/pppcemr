# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-25 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0135_cptcode_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatmentoption',
            name='cpt',
        ),
    ]
