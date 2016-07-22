# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0051_workplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkplanStepAddAssessment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('diagnosis', models.ForeignKey(to='pppcemr.Diagnosis')),
            ],
        ),
        migrations.RemoveField(
            model_name='workplan',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='workplan',
            name='lab',
        ),
        migrations.AddField(
            model_name='workplanstepaddassessment',
            name='workplan',
            field=models.ForeignKey(to='pppcemr.Workplan'),
        ),
    ]
