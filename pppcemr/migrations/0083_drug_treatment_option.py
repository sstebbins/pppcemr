# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0082_auto_20160221_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='treatment_option',
            field=models.ForeignKey(blank=True, to='pppcemr.TreatmentOption', null=True),
        ),
    ]
