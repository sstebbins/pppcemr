# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0126_delete_vaccinecomponent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vaccineantigen',
            options={'ordering': ['-name']},
        ),
    ]
