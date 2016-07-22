# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
        ('pppcemr', '0030_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assessment',
            field=models.ForeignKey(to='pppcemr.Assessment', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='body',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 10, 19, 4, 15, 316114, tzinfo=utc), verbose_name='date and time of treatment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='encounter',
            field=models.ForeignKey(to='pppcemr.Encounter', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='task_owners'),
        ),
        migrations.AddField(
            model_name='task',
            name='owner_group',
            field=models.ForeignKey(to='auth.Group', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='patient',
            field=models.ForeignKey(default=1, to='pppcemr.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='task_senders'),
        ),
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.CharField(max_length=300),
        ),
    ]
