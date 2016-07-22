# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0024_auto_20151014_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='InHouseLab',
            fields=[
                ('treatment_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='pppcemr.Treatment', serialize=False, auto_created=True)),
                ('result', models.TextField(null=True, blank=True)),
            ],
            bases=('pppcemr.treatment',),
        ),
        migrations.CreateModel(
            name='InHouseLabType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('test_name', models.CharField(max_length=100)),
                ('cpt', models.CharField(max_length=10)),
                ('default_result', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='lab',
            name='result',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inhouselab',
            name='inhouselabtype',
            field=models.ForeignKey(to='pppcemr.InHouseLabType'),
        ),
    ]
