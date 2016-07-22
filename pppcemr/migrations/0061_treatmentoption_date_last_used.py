# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0060_auto_20160204_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentoption',
            name='date_last_used',
            field=models.DateTimeField(verbose_name='date last used', default=datetime.datetime(2016, 2, 4, 17, 14, 9, 396257, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
