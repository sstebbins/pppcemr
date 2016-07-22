# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0052_auto_20151125_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkplanStepAddInHouseLab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('lab_type', models.ForeignKey(to='pppcemr.InHouseLabType')),
                ('workplan', models.ForeignKey(to='pppcemr.Workplan')),
            ],
        ),
        migrations.CreateModel(
            name='WorkplanStepAddLab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('lab_type', models.ForeignKey(to='pppcemr.LabType')),
                ('workplan', models.ForeignKey(to='pppcemr.Workplan')),
            ],
        ),
    ]
