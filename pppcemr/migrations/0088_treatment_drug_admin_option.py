# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0087_auto_20160222_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='drug_admin_option',
            field=models.ForeignKey(blank=True, to='pppcemr.DrugAdminOption', null=True),
        ),
    ]
