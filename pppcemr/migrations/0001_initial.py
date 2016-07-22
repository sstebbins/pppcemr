# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encounter_type', models.CharField(max_length=50)),
                ('encounter_date', models.DateTimeField(verbose_name=b'date of encounter')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birthdate', models.DateTimeField(verbose_name=b'birthdate')),
            ],
        ),
        migrations.AddField(
            model_name='encounter',
            name='patient',
            field=models.ForeignKey(to='pppcemr.Patient'),
        ),
    ]
