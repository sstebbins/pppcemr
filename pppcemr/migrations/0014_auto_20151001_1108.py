# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0013_auto_20150930_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name_plural': 'diagnoses'},
        ),
        migrations.AlterField(
            model_name='encounter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
