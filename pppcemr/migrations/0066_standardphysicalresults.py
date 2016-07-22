# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0065_workplanstepaddtreatment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPhysicalResults',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('PE_constitutional', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_head_and_face', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_eyes', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_ears', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_nose_mouth_and_throat', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_neck', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_chest_and_breast', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_respiratory', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_heart', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_pulses_vascular', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_gastrointestinal', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_GU', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_musculoskeletal', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_skin_and_nodes', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_neurologic', models.CharField(blank=True, null=True, max_length=200)),
                ('PE_psyche', models.CharField(blank=True, null=True, max_length=200)),
            ],
        ),
    ]
