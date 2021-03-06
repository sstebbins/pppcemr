# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-07 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import pppcemr.models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0155_auto_20160707_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileattachment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date and time of upload'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fileattachment',
            name='file_attachment',
            field=models.FileField(upload_to=pppcemr.models.attachment_directory_path),
        ),
    ]
