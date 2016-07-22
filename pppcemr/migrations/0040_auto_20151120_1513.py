# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0039_auto_20151116_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name_plural': 'diagnoses'},
        ),
        migrations.AddField(
            model_name='encounter',
            name='office',
            field=models.ForeignKey(null=True, to='pppcemr.Office', blank=True),
        ),
    ]
