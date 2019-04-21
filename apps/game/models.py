from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Game(models.Model):
    """
    Игра
    Модель используется как для организации процесса игры, так и для хранения её результата
    """

    STATES = (
        (0, _('WAITING FOR PLAYERS')),
        (1, _('IN GAME BUT FIRST IS ENDED')),
        (2, _('IN GAME BUT SECOND IS ENDED')),
        (3, _('IN GAME')),
        (100, _('GAME IS ENDED'))
    )

    player1 = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Player 1'))
    player2 = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Player 2'))
    winner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Winner'))
    loser = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Loser'))
    winner_points = models.IntegerField(blank=False, null=True, default=0, verbose_name=_('Winner points'))
    loser_points = models.IntegerField(blank=False, null=True, default=0, verbose_name=_('Loser points'))
    start = models.DateTimeField(blank=False, auto_now_add=True, verbose_name=_('Game start time'))
    end = models.DateTimeField(blank=False, verbose_name=_('Game end time'))
    state = models.IntegerField(blank=False, null=False, choices=STATES, default=0, verbose_name=_('State'))

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')

    def __str__(self):
        return self.__class__.__name__