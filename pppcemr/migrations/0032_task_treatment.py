# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0031_auto_20151110_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='treatment',
            field=models.ForeignKey(blank=True, null=True, to='pppcemr.Treatment'),
        ),
    ]
