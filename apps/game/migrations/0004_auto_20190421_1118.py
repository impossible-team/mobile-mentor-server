# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-21 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190421_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameresults',
            name='player_1',
        ),
        migrations.RemoveField(
            model_name='gameresults',
            name='player_2',
        ),
        migrations.AddField(
            model_name='gameresults',
            name='player1',
            field=models.BooleanField(default=False, verbose_name='Player 1'),
        ),
        migrations.AddField(
            model_name='gameresults',
            name='player2',
            field=models.BooleanField(default=False, verbose_name='Player 2'),
        ),
    ]
