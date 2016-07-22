# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0019_encounter_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=1, default='M', choices=[('M', 'Male'), ('F', 'Female')]),
            preserve_default=False,
        ),
    ]
