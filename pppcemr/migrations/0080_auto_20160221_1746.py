# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0079_drug_drugpackage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='ndc_product_ID',
            new_name='product_ID',
        ),
        migrations.AddField(
            model_name='drug',
            name='product_ndc',
            field=models.CharField(max_length=25, default=1),
            preserve_default=False,
        ),
    ]
