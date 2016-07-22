# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0094_auto_20160226_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='dispense_unit',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
    ]
