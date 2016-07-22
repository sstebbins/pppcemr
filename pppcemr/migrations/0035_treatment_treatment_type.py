# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0034_treatment_next_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='treatment_type',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
    ]
