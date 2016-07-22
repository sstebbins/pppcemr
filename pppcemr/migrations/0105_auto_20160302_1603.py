# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0104_auto_20160302_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugadminoption',
            name='frequency',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Daily PRN', 'Daily PRN'), ('BID', 'BID'), ('BID PRN', 'BID PRN'), ('TID', 'TID'), ('TID PRN', 'TID PRN'), ('QID', 'QID'), ('QID PRN', 'QID PRN'), ('Q2H', 'Q2H'), ('Q2H PRN', 'Q2H PRN'), ('Q4H', 'Q4H'), ('Q4H PRN', 'Q4H PRN'), ('Q6H', 'Q6H'), ('Q6H PRN', 'Q6H PRN'), ('Q8H', 'Q8H'), ('Q8H PRN', 'Q8H PRN'), ('Q12H', 'Q12H'), ('Q12H PRN', 'Q12H PRN'), ('ASDIR', 'As Directed')], max_length=10),
        ),
    ]
