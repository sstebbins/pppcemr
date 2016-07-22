# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('pppcemr', '0041_task_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=100)),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
        ),
    ]
