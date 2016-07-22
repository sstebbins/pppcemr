# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-09 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0157_encounter_final_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicepreferences',
            name='encounter_summary_report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='encounter_summary_report', to='pppcemr.Report'),
            preserve_default=False,
        ),
    ]