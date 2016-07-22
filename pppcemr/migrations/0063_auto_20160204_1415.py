# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0062_auto_20160204_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='BP_location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='Diastolic_BP',
            field=models.IntegerField(blank=True, help_text='mmHg', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='HR',
            field=models.IntegerField(blank=True, help_text='BPM', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='RR',
            field=models.IntegerField(blank=True, help_text='breaths per min', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='Systolic_BP',
            field=models.IntegerField(blank=True, help_text='mmHg', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='chief_complaint',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='height',
            field=models.FloatField(blank=True, help_text='in', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='temperature',
            field=models.FloatField(blank=True, help_text='F', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='temperature_location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='weight_lb',
            field=models.FloatField(blank=True, help_text='lb', null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='weight_oz',
            field=models.FloatField(blank=True, help_text='oz', null=True),
        ),
    ]
