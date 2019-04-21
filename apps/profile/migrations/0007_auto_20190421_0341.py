# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-21 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0006_auto_20190421_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='guid',
            field=models.UUIDField(default=uuid.UUID('34ea30d3-fedb-46eb-91f6-132df5d2ca7a'), verbose_name='UUID'),
        ),
    ]
