# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0071_treatment_diagnosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='diagnosis',
            field=models.ManyToManyField(blank=True, to='pppcemr.Diagnosis'),
        ),
    ]
