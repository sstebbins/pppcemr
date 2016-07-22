# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0004_assessment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='icd10_code',
            field=models.CharField(max_length=10, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='icd9_code',
            field=models.CharField(max_length=10, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='snomed_code',
            field=models.CharField(max_length=10, default=0),
            preserve_default=False,
        ),
    ]
