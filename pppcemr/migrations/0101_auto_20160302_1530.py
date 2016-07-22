# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0100_auto_20160302_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='route',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
