# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0086_drugadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugAdminOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('frequency', models.CharField(max_length=5, choices=[('QD', 'Daily'), ('BID', 'Twice Daily'), ('TID', 'Three Times Daily'), ('ASDIR', 'As Directed')])),
                ('treatment_option', models.ForeignKey(blank=True, to='pppcemr.TreatmentOption', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DrugAdmin',
        ),
    ]
