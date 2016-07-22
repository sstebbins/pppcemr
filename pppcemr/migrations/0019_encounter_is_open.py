# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0018_remove_encountertype_general_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]
