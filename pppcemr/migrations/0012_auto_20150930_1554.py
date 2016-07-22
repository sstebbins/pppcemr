# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0011_auto_20150926_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='encounter',
        ),
        migrations.AddField(
            model_name='assessment',
            name='encounter',
            field=models.ForeignKey(null=True, to='pppcemr.Encounter', blank=True),
        ),
    ]
