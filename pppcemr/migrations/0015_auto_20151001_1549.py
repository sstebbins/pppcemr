# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0014_auto_20151001_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncounterType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='encounter',
            name='encounter_type',
            field=models.ForeignKey(blank=True, null=True, to='pppcemr.EncounterType'),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID'),
        ),
    ]
