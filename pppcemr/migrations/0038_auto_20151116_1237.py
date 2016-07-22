# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0037_auto_20151116_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='encounter_owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='encounter',
            name='encounter_type',
            field=models.ForeignKey(to='pppcemr.EncounterType', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='treatment',
            name='description',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='treatment',
            name='encounter',
            field=models.ForeignKey(to='pppcemr.Encounter', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='treatment',
            name='next_page',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='treatment',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
