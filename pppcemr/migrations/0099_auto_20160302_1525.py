# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0098_treatment_drug_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugadminoption',
            name='PRN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='drugadminoption',
            name='PRN_indication',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='drugadminoption',
            name='patient_instruction',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='drugadminoption',
            name='pharmacist_instruction',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PRN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PRN_indication',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='patient_instruction',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='pharmacist_instruction',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='drugadminoption',
            name='frequency',
            field=models.CharField(max_length=5, choices=[('QD', 'Daily'), ('BID', 'BID'), ('TID', 'TID'), ('QID', 'QID'), ('Q2H', 'Q2H'), ('Q4H', 'Q4h'), ('ASDIR', 'As Directed')]),
        ),
    ]
