# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxbets_app', '0003_auto_20180305_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]