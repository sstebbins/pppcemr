# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0095_treatment_dispense_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('product_ndc', models.CharField(max_length=25)),
                ('package_ndc', models.CharField(max_length=25)),
                ('package_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='treatment',
            name='duration',
            field=models.IntegerField(null=True, help_text='(days)', blank=True),
        ),
    ]
