# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0093_auto_20160226_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='duration',
            field=models.IntegerField(blank=True, null=True, max_length=20),
        ),
    ]
