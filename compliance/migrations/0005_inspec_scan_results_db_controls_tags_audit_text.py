# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-08 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0004_auto_20190308_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspec_scan_results_db',
            name='controls_tags_audit_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
