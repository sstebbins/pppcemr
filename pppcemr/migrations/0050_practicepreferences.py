# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('pppcemr', '0049_remove_lab_group_recipient_for_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticePreferences',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('group_to_receive_new_lab_tasks', models.ForeignKey(to='auth.Group')),
            ],
        ),
    ]
