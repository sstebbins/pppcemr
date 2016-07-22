# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0106_snomed'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='user_description',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
    ]
