# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('pppcemr', '0047_auto_20151124_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='task_group_recipient',
        ),
        migrations.AddField(
            model_name='lab',
            name='group_recipient_for_task',
            field=models.ForeignKey(default=1, to='auth.Group'),
            preserve_default=False,
        ),
    ]
