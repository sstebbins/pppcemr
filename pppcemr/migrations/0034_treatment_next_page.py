# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0033_task_next_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='next_page',
            field=models.URLField(blank=True, null=True),
        ),
    ]
