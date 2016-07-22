# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0061_treatmentoption_date_last_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='date_last_used',
            field=models.DateTimeField(blank=True, verbose_name='date last used', null=True),
        ),
        migrations.AlterField(
            model_name='treatmentoption',
            name='date_last_used',
            field=models.DateTimeField(blank=True, verbose_name='date last used', null=True),
        ),
    ]
