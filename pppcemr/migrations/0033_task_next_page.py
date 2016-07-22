# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0032_task_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='next_page',
            field=models.URLField(null=True, blank=True),
        ),
    ]
