# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0002_auto_20150827_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='encounter_date',
            field=models.DateTimeField(verbose_name='date and time of encounter'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(verbose_name='birthdate'),
        ),
    ]
