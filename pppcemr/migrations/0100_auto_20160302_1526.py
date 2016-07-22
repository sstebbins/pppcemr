# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0099_auto_20160302_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugadminoption',
            name='PRN',
        ),
        migrations.RemoveField(
            model_name='drugadminoption',
            name='PRN_indication',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='PRN',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='PRN_indication',
        ),
    ]
