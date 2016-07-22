# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0036_auto_20151116_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='diagnosis',
            field=models.ForeignKey(to='pppcemr.Diagnosis', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='encounter',
            field=models.ForeignKey(to='pppcemr.Encounter', default=1),
            preserve_default=False,
        ),
    ]
