# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0089_auto_20160223_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='total_weight',
            field=models.FloatField(help_text='oz', null=True, blank=True),
        ),
    ]
