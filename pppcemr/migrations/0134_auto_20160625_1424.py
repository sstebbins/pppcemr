# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-25 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0133_auto_20160617_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPTcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pppcemr.TreatmentOption')),
            ],
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='cpt',
        ),
    ]
