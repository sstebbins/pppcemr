# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0077_auto_20160218_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='date and time of treatment', blank=True),
        ),
    ]
