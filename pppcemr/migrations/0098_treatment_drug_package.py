# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0097_auto_20160302_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='drug_package',
            field=models.ForeignKey(null=True, to='pppcemr.DrugPackage', blank=True),
        ),
    ]
