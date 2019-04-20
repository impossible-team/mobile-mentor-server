# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20190421_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='guid',
            field=models.UUIDField(default=uuid.UUID('884ac1d5-112c-498c-b51b-85ef18723357'), verbose_name='UUID'),
        ),
    ]
