# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0007_auto_20150901_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encounter',
            old_name='enocounter_owner',
            new_name='encounter_owner',
        ),
    ]
