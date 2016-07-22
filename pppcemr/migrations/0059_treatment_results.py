# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0058_auto_20160128_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='results',
            field=models.TextField(null=True),
        ),
    ]
