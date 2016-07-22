# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0017_auto_20151001_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encountertype',
            name='general_type',
        ),
    ]
