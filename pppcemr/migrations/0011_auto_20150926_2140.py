# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0010_encounter_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='icd10_code',
            new_name='icd_code',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='icd9_code',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='snomed_code',
        ),
    ]
