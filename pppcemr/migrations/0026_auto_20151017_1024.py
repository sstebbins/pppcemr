# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0025_auto_20151015_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='assessment',
        ),
        migrations.AddField(
            model_name='treatment',
            name='assessment',
            field=models.ManyToManyField(blank=True, null=True, to='pppcemr.Assessment'),
        ),
    ]
