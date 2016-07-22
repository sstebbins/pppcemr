# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0096_auto_20160302_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatment',
            old_name='drug_package',
            new_name='drug',
        ),
    ]
