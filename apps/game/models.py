from django.db import models
from django.utils.translation import ugettext_lazy as _
from profile.models import Profile
from topic.models import Test


class Game(models.Model):
    """
    Игра
    Модель используется как для организации процесса игры, так и для хранения её результата
    """
    STATE_WAITING_FOR_PLAYERS = 0
    STATE_IN_GAME = 3
    STATE_GAME_IS_ENDED = 100

    STATES = (
        (0, _('WAITING FOR PLAYERS')),
        (1, _('IN GAME BUT FIRST IS ENDED')),
        (2, _('IN GAME BUT SECOND IS ENDED')),
        (3, _('IN GAME')),
        (100, _('GAME IS ENDED'))
    )

    player1 = models.OneToOneField(Profile, null=True, related_name='+', on_delete=models.CASCADE, verbose_name=_('Player 1'))
    player2 = models.OneToOneField(Profile, null=True, related_name='+', on_delete=models.CASCADE, verbose_name=_('Player 2'))
    winner = models.OneToOneField(Profile, null=True, related_name='winner_games_set', on_delete=models.CASCADE, verbose_name=_('Winner'))
    loser = models.OneToOneField(Profile, null=True, related_name='loser_games_set', on_delete=models.CASCADE, verbose_name=_('Loser'))
    winner_points = models.IntegerField(null=True, default=0, verbose_name=_('Winner points'))
    loser_points = models.IntegerField(null=True, default=0, verbose_name=_('Loser points'))
    start_time = models.DateTimeField(null=True, auto_now_add=True, verbose_name=_('Game start time'))
    end_time = models.DateTimeField(null=True, verbose_name=_('Game end time'))
    state = models.IntegerField(null=False, choices=STATES, default=0, verbose_name=_('State'))
    results = models.ManyToManyField(Test, through='GameResults', through_fields=('game', 'test'))

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')

    def __str__(self):
        return self.__class__.__name__


class GameResults(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name=_('Game'))
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_('Test'))
    player_1 = models.BooleanField(null=False, blank=False, default=False, verbose_name=_('Player 1'))
    player_2 = models.BooleanField(null=False, blank=False, default=False, verbose_name=_('Player 2'))

    class Meta:
        verbose_name = _('Game result')
        verbose_name_plural = _('Game results')
