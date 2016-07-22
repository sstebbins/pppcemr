# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0038_auto_20151116_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'ordering': ['-date_last_used'], 'verbose_name_plural': 'diagnoses'},
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='date_last_used',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 16, 20, 20, 48, 432036, tzinfo=utc), verbose_name='date last used'),
            preserve_default=False,
        ),
    ]
