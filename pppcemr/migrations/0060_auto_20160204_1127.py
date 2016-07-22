# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0059_treatment_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentoption',
            name='cpt',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
    ]
