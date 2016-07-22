# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0022_auto_20151013_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='treatment_type',
        ),
        migrations.AddField(
            model_name='treatment',
            name='description',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='TreatmentType',
        ),
    ]
