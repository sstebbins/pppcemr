# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pppcemr', '0023_auto_20151014_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('treatment_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='pppcemr.Treatment', auto_created=True)),
                ('result', models.TextField()),
            ],
            bases=('pppcemr.treatment',),
        ),
        migrations.CreateModel(
            name='LabType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('cpt', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('treatment_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='pppcemr.Treatment', auto_created=True)),
                ('note_text', models.TextField()),
            ],
            bases=('pppcemr.treatment',),
        ),
        migrations.AddField(
            model_name='assessment',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lab',
            name='labtype',
            field=models.ForeignKey(to='pppcemr.LabType'),
        ),
    ]
