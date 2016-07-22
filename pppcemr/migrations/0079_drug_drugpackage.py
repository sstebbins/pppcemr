# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0078_auto_20160218_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trade_name', models.CharField(max_length=100)),
                ('generic_name', models.CharField(max_length=100)),
                ('ndc_product_ID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DrugPackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ndc_package_code', models.CharField(max_length=100)),
                ('drug', models.ForeignKey(to='pppcemr.Drug')),
            ],
        ),
    ]
