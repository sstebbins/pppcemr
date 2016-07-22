# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0050_practicepreferences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('is_well', models.BooleanField(default=True)),
                ('assessment', models.ManyToManyField(to='pppcemr.Assessment', blank=True)),
                ('lab', models.ManyToManyField(to='pppcemr.Lab', blank=True)),
            ],
        ),
    ]
