# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0074_auto_20160218_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='results',
            field=models.TextField(null=True, blank=True),
        ),
    ]
