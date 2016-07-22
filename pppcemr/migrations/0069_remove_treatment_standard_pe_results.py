# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0068_auto_20160215_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='standard_PE_results',
        ),
    ]
