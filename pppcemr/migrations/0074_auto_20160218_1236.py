# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0073_auto_20160218_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='date',
            field=models.DateTimeField(blank=True, verbose_name='date and time of treatment', null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='encounter',
            field=models.ForeignKey(blank=True, to='pppcemr.Encounter', null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='next_page',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(blank=True, to='pppcemr.Patient', null=True),
        ),
    ]
