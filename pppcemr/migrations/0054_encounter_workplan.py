# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0053_workplanstepaddinhouselab_workplanstepaddlab'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='workplan',
            field=models.ForeignKey(to='pppcemr.Workplan', blank=True, null=True),
        ),
    ]
