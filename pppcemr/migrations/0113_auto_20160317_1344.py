# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0112_workplanstepaddtask_encounter_owner_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='auto_close',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='auto_close',
            field=models.BooleanField(default=False),
        ),
    ]