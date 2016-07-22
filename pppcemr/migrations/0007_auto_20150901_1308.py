# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0006_encounter_enocounter_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='encounter',
        ),
        migrations.AddField(
            model_name='assessment',
            name='encounter',
            field=models.ManyToManyField(to='pppcemr.Encounter'),
        ),
    ]
