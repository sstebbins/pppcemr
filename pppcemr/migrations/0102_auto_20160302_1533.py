# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0101_auto_20160302_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugadminoption',
            name='frequency',
            field=models.CharField(max_length=10, choices=[('QD', 'Daily'), ('BID', 'BID'), ('TID', 'TID'), ('QID', 'QID'), ('Q2H', 'Q2H'), ('Q4H', 'Q4H'), ('Q6H', 'Q6H'), ('Q8H', 'Q8H'), ('Q12H', 'Q12H'), ('ASDIR', 'As Directed')]),
        ),
    ]
