# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0125_treatmentoption_vaccine_antigens'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VaccineComponent',
        ),
    ]
