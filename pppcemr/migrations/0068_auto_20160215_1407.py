# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0067_auto_20160215_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='standard_PE_results',
            field=models.ForeignKey(blank=True, null=True, to='pppcemr.StandardPhysicalResults'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='treatment_option',
            field=models.ForeignKey(to='pppcemr.TreatmentOption', default=1),
            preserve_default=False,
        ),
    ]
