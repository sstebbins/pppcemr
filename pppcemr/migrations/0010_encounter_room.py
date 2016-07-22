# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0009_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='room',
            field=models.ForeignKey(blank=True, null=True, to='pppcemr.Room'),
        ),
    ]
