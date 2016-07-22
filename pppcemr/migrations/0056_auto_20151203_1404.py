# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0055_vitals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vitals',
            old_name='DBP',
            new_name='Diastolic_BP',
        ),
        migrations.RenameField(
            model_name='vitals',
            old_name='SBP',
            new_name='Systolic_BP',
        ),
    ]
