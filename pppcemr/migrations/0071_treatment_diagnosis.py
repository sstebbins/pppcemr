# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0070_treatment_standard_pe_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='diagnosis',
            field=models.ManyToManyField(null=True, blank=True, to='pppcemr.Diagnosis'),
        ),
    ]
