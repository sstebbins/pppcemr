# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0003_auto_20150827_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('assessment_date', models.DateTimeField(verbose_name='date and time of assessment')),
                ('encounter', models.ForeignKey(to='pppcemr.Encounter')),
                ('patient', models.ForeignKey(to='pppcemr.Patient')),
            ],
        ),
    ]
