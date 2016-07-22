# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0090_treatment_total_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugadminoption',
            name='duration_days',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='treatment',
            name='frequency',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='route',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
    ]
