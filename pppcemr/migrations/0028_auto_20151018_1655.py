# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0027_auto_20151017_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labtype',
            options={'verbose_name': 'lab type'},
        ),
        migrations.RenameField(
            model_name='lab',
            old_name='labtype',
            new_name='lab_type',
        ),
    ]
