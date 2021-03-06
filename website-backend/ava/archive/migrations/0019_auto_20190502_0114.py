# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-02 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0018_auto_20170831_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='exposure_ms',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='project',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='session',
            name='invert_polarization',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='session',
            name='session_master_calib',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='archive.Take'),
        ),
        migrations.AddField(
            model_name='session',
            name='session_master_colorchart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='archive.Take'),
        ),
        migrations.AddField(
            model_name='session',
            name='session_neutral_take',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='archive.Take'),
        ),
        migrations.AddField(
            model_name='staticscanasset',
            name='associated_tracking_asset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staticscanasset_related', to='archive.TrackingAsset'),
        ),
        migrations.AddField(
            model_name='staticscanasset',
            name='associated_tracking_asset_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staticscanasset',
            name='has_tracking',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='take',
            name='colorspace',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='take',
            name='is_burst',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='take',
            name='is_scan_burst',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='take',
            name='work_folder',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='trackingasset',
            name='work_folder',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='take',
            name='flag',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], db_index=True, default='none', max_length=100, no_check_for_status=True),
        ),
        migrations.AlterField(
            model_name='trackingasset',
            name='calib_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
