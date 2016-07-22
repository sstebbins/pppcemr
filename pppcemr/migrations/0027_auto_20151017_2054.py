# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0026_auto_20151017_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='assessment',
        ),
        migrations.AddField(
            model_name='treatment',
            name='assessment',
            field=models.ForeignKey(blank=True, to='pppcemr.Assessment', null=True),
        ),
    ]
