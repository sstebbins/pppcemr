# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0103_auto_20160302_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugadminoption',
            name='frequency',
            field=models.CharField(choices=[('QD', 'Daily'), ('QDPRN', 'Daily PRN'), ('BID', 'BID'), ('BIDPRN', 'BID PRN'), ('TID', 'TID'), ('TIDPRN', 'TID PRN'), ('QID', 'QID'), ('QIDPRN', 'QID PRN'), ('Q2H', 'Q2H'), ('Q2HPRN', 'Q2H PRN'), ('Q4H', 'Q4H'), ('Q4HPRN', 'Q4H PRN'), ('Q6H', 'Q6H'), ('Q6H PRN', 'Q6H PRN'), ('Q8H', 'Q8H'), ('Q8H PRN', 'Q8H PRN'), ('Q12H', 'Q12H'), ('Q12HPRN', 'Q12H PRN'), ('ASDIR', 'As Directed')], max_length=10),
        ),
    ]
