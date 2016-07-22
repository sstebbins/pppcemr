# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0012_auto_20150930_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('icd_code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='icd_code',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='name',
        ),
        migrations.AddField(
            model_name='assessment',
            name='diagnosis',
            field=models.ForeignKey(blank=True, null=True, to='pppcemr.Diagnosis'),
        ),
    ]
