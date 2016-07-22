# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0015_auto_20151001_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='encountertype',
            name='general_type',
            field=models.CharField(choices=[('SI', 'Sick'), ('WE', 'Well')], default='SI', max_length=50),
        ),
    ]
