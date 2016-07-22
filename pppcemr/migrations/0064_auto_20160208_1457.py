# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0063_auto_20160204_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='PE_GU',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_chest_and_breast',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_constitutional',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_ears',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_eyes',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_gastrointestinal',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_head_and_face',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_heart',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_musculoskeletal',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_neck',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_neurologic',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_nose_mouth_and_throat',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_psyche',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_pulses_vascular',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_respiratory',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='PE_skin_and_nodes',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='birth_history',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='family_history',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='past_medical_history',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='social_history',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='surgical_and_hospital_history',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='BP_location',
            field=models.CharField(null=True, max_length=20, help_text='LA, RA, etc', blank=True),
        ),
        migrations.AlterField(
            model_name='treatmentoption',
            name='type',
            field=models.CharField(choices=[('NT', 'Note'), ('LB', 'Lab'), ('IL', 'In House Lab'), ('VI', 'Vital Signs'), ('RX', 'Drug Prescription'), ('PR', 'Procedure'), ('TS', 'Test'), ('HP', 'HPI and ROS'), ('PE', 'Physical Exam'), ('PF', 'PFSH'), ('FU', 'Follow-up Instructions')], max_length=2, default='NT'),
        ),
    ]
