# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-10 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0011_auto_20170405_1049'),
        ('jobs', '0016_farmjob_req_gpu'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmjob',
            name='ext_tracking_assets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ext_jobs', to='archive.TrackingAsset'),
        ),
    ]
