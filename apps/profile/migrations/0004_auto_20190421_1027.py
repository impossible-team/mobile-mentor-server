# Generated by Django 2.2 on 2019-04-21 07:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20190421_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='guid',
            field=models.UUIDField(default=uuid.UUID('926bf93d-5ed3-4241-add4-d3d3312b1534'), verbose_name='UUID'),
        ),
    ]
