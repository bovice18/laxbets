# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 04:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laxbets_app', '0006_auto_20180305_2339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeeklyPicks',
            new_name='PlayerSubmission',
        ),
    ]