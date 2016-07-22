# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0046_lab_task_group_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='task_group_recipient',
            field=models.ForeignKey(related_name='task_group_recipient', to='auth.Group'),
        ),
    ]
