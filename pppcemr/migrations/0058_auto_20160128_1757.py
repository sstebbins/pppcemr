# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0057_auto_20151203_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('default_result', models.TextField(null=True, blank=True)),
                ('type', models.CharField(default='NT', max_length=2, choices=[('NT', 'Note'), ('LB', 'Lab'), ('IL', 'In House Lab'), ('VI', 'Vital Signs'), ('RX', 'Drug Prescription'), ('PR', 'Procedure'), ('TS', 'Test')])),
                ('cpt', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'treatment option',
            },
        ),
        migrations.RemoveField(
            model_name='inhouselab',
            name='inhouselabtype',
        ),
        migrations.RemoveField(
            model_name='inhouselab',
            name='treatment_ptr',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='lab_type',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='treatment_ptr',
        ),
        migrations.RemoveField(
            model_name='note',
            name='treatment_ptr',
        ),
        migrations.RemoveField(
            model_name='vitals',
            name='treatment_ptr',
        ),
        migrations.RemoveField(
            model_name='workplanstepaddinhouselab',
            name='lab_type',
        ),
        migrations.RemoveField(
            model_name='workplanstepaddinhouselab',
            name='workplan',
        ),
        migrations.RemoveField(
            model_name='workplanstepaddlab',
            name='lab_type',
        ),
        migrations.RemoveField(
            model_name='workplanstepaddlab',
            name='workplan',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='treatment_type',
        ),
        migrations.AddField(
            model_name='treatment',
            name='cpt',
            field=models.CharField(blank=True, null=True, max_length=10),
        ),
        migrations.DeleteModel(
            name='InHouseLab',
        ),
        migrations.DeleteModel(
            name='InHouseLabType',
        ),
        migrations.DeleteModel(
            name='Lab',
        ),
        migrations.DeleteModel(
            name='LabType',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Vitals',
        ),
        migrations.DeleteModel(
            name='WorkplanStepAddInHouseLab',
        ),
        migrations.DeleteModel(
            name='WorkplanStepAddLab',
        ),
        migrations.AddField(
            model_name='treatment',
            name='treatment_option',
            field=models.ForeignKey(to='pppcemr.TreatmentOption', default=1),
            preserve_default=False,
        ),
    ]
