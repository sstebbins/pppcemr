# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0066_standardphysicalresults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='treatment_option',
            field=models.ForeignKey(to='pppcemr.TreatmentOption', blank=True, null=True),
        ),
    ]
