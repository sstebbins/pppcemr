# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0081_auto_20160221_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='product_ID',
            new_name='product_id',
        ),
        migrations.AddField(
            model_name='treatment',
            name='drug_package',
            field=models.ForeignKey(to='pppcemr.Drug', null=True, blank=True),
        ),
    ]
