# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0044_auto_20151124_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='task_group_recipient',
        ),
    ]
