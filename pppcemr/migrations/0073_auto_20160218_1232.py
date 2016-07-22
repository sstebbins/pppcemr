# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0072_auto_20160218_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='diagnosis',
        ),
        migrations.AddField(
            model_name='treatment',
            name='diagnosis',
            field=models.ForeignKey(blank=True, to='pppcemr.Diagnosis', null=True),
        ),
    ]
