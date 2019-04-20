# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20190420_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='guid',
            field=models.UUIDField(default=uuid.UUID('213f6e6f-8c75-4e39-81de-99ca025ca9fd'), verbose_name='UUID'),
        ),
    ]
