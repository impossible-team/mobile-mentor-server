# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-21 00:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('profile', '0001_initial'), ('profile', '0002_auto_20190420_1936'), ('profile', '0003_auto_20190421_0051'), ('profile', '0004_auto_20190421_0052'), ('profile', '0005_auto_20190421_0053'), ('profile', '0006_auto_20190421_0243'), ('profile', '0007_auto_20190421_0341')]

    dependencies = [
        ('topic', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.UUID('34ea30d3-fedb-46eb-91f6-132df5d2ca7a'), verbose_name='UUID')),
                ('state', models.IntegerField(choices=[(0, 'OFFLINE'), (1, 'ONLINE'), (2, 'READY TO PLAY'), (3, 'IN GAME')], default=0, verbose_name='State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('points', models.PositiveIntegerField(default=0, verbose_name='Points')),
                ('blocks', models.ManyToManyField(to='topic.Block', verbose_name='Blocks')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
