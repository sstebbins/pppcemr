# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0020_patient_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(verbose_name='date and time of assessment')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='assessment',
            field=models.ForeignKey(blank=True, null=True, to='pppcemr.Assessment'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='encounter',
            field=models.ForeignKey(blank=True, null=True, to='pppcemr.Encounter'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(to='pppcemr.Patient'),
        ),
    ]
