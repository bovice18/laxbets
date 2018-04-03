# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laxbets_app', '0004_auto_20180305_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='submission',
            name='weekof',
        ),
        migrations.AlterField(
            model_name='game',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='underdog_team', to='laxbets_app.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_team', to='laxbets_app.Team'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='pick',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laxbets_app.Team'),
        ),
        migrations.AddField(
            model_name='playerweek',
            name='picks',
            field=models.ManyToManyField(to='laxbets_app.Submission'),
        ),
        migrations.AddField(
            model_name='playerweek',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laxbets_app.Week'),
        ),
    ]