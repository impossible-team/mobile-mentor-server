# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('short_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('correct_answer_code', models.PositiveIntegerField(default=0, verbose_name='Correct answer')),
                ('block', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='topic.Block', verbose_name='Block')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='topic.Topic', verbose_name='Topic'),
        ),
    ]