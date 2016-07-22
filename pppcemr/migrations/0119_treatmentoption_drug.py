# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0118_remove_drug_treatment_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentoption',
            name='drug',
            field=models.ManyToManyField(blank=True, to='pppcemr.Drug'),
        ),
    ]
