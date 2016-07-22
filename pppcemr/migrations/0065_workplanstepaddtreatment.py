# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0064_auto_20160208_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkplanStepAddTreatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('treatment_option', models.ForeignKey(to='pppcemr.TreatmentOption')),
                ('workplan', models.ForeignKey(to='pppcemr.Workplan')),
            ],
        ),
    ]
