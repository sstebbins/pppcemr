# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0083_drug_treatment_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugpackage',
            name='drug',
        ),
        migrations.DeleteModel(
            name='DrugPackage',
        ),
    ]
