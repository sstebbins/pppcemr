# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0069_remove_treatment_standard_pe_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='standard_PE_results',
            field=models.ForeignKey(blank=True, to='pppcemr.StandardPhysicalResults', null=True),
        ),
    ]
