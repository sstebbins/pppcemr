# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('pppcemr', '0042_employeegroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='task_group_recipient',
            field=models.ForeignKey(to_field='Group to receive task', to='auth.Group', default=datetime.datetime(2015, 11, 24, 17, 59, 12, 48523, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
