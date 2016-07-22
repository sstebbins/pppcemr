# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0048_auto_20151124_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='group_recipient_for_task',
        ),
    ]
