# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0080_auto_20160221_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='concentration_denominator',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='concentration_numerator',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='dea',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='dosage_form',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drug',
            name='route',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drug',
            name='generic_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='drug',
            name='trade_name',
            field=models.CharField(max_length=500),
        ),
    ]
