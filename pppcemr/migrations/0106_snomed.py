# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0105_auto_20160302_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snomed',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=100)),
                ('icd_equivalents', models.CharField(max_length=500)),
            ],
        ),
    ]
