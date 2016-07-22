# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0021_auto_20151008_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('cpt', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='description',
        ),
        migrations.AlterField(
            model_name='treatment',
            name='date',
            field=models.DateTimeField(verbose_name='date and time of treatment'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='treatment_type',
            field=models.ForeignKey(blank=True, to='pppcemr.TreatmentType', null=True),
        ),
    ]
