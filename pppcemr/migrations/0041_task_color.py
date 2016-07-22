# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0040_auto_20151120_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(null=True, blank=True, max_length=20),
        ),
    ]
