# Generated by Django 2.2 on 2019-04-21 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='end',
        ),
        migrations.RemoveField(
            model_name='game',
            name='start',
        ),
        migrations.AddField(
            model_name='game',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='Game end time'),
        ),
        migrations.AddField(
            model_name='game',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Game start time'),
        ),
        migrations.AlterField(
            model_name='game',
            name='loser',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loser_games_set', to='profile.Profile', verbose_name='Loser'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profile.Profile', verbose_name='Player 1'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player2',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profile.Profile', verbose_name='Player 2'),
        ),
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner_games_set', to='profile.Profile', verbose_name='Winner'),
        ),
    ]