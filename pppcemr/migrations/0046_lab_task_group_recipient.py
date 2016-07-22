# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('pppcemr', '0045_remove_lab_task_group_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='task_group_recipient',
            field=models.ForeignKey(default=1, to='auth.Group'),
            preserve_default=False,
        ),
    ]
