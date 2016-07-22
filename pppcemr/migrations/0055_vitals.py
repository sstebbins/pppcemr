# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0054_encounter_workplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('treatment_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to='pppcemr.Treatment')),
                ('chief_complaint', models.TextField()),
                ('weight_lb', models.FloatField(blank=True, null=True, help_text='lb')),
                ('weight_oz', models.FloatField(blank=True, null=True, help_text='lb')),
                ('height', models.FloatField(blank=True, null=True, help_text='in')),
                ('temperature', models.FloatField(blank=True, null=True, help_text='F')),
                ('temperature_location', models.CharField(max_length=20)),
                ('HR', models.IntegerField(blank=True, null=True, help_text='BPM')),
                ('RR', models.IntegerField(blank=True, null=True, help_text='breaths per min')),
                ('SBP', models.IntegerField(blank=True, null=True, help_text='mmHg')),
                ('DBP', models.IntegerField(blank=True, null=True, help_text='mmHg')),
                ('BP_location', models.CharField(max_length=20)),
            ],
            bases=('pppcemr.treatment',),
        ),
    ]
