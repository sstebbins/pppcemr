# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0091_auto_20160225_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='duration',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
    ]
