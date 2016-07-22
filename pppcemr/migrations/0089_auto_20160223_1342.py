# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0088_treatment_drug_admin_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugadminoption',
            name='dose',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='drugadminoption',
            name='dose_per_day',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='drugadminoption',
            name='multiply_by_weight',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='calculated_dose',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='dose_unit',
            field=models.CharField(max_length=10, blank=True, null=True),
        ),
    ]
