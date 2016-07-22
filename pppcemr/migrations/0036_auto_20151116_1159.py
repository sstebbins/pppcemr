# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0035_treatment_treatment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='treatment_type',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]
