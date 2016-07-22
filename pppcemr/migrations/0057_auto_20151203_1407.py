# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0056_auto_20151203_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitals',
            name='temperature_location',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
