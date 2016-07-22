# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0092_treatment_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='dispense_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='drugadminoption',
            name='duration_days',
            field=models.IntegerField(default=0),
        ),
    ]
