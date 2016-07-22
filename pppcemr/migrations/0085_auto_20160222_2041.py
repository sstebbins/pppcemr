# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0084_auto_20160222_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='dea',
            field=models.CharField(max_length=25, blank=True, null=True),
        ),
    ]
