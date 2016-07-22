# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0076_auto_20160218_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 18, 17, 43, 22, 2818, tzinfo=utc), verbose_name='date and time of treatment'),
            preserve_default=False,
        ),
    ]
