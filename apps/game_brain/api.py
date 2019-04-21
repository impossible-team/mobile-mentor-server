from random import shuffle
from django.db.models import Q

from game.models import Game, GameResults
from topic.models import Test


TESTS_COUNT = 3


def get_game(player):
    player_now_play = Game.objects.order_by('?').filter(Q(player1=player) | Q(player2=player), ~Q(state=Game.STATE_GAME_IS_ENDED))

    if player_now_play:
        return player_now_play[0]

    # поиск случайной свободной игры
    wainting_payers = Game.objects.order_by('?').filter(state__exact=Game.STATE_WAITING_FOR_PLAYERS)
    # waiter_players = Profile.objects.order_by('?').filter(state__exact=Profile.STATE_READY_TO_PLAY)
    if wainting_payers:
        g = wainting_payers[0]  # type: Game
        g.state = Game.STATE_IN_GAME
        g.player2 = player
        g.save()
        return g
    new_game = Game.objects.create(player1=player)
    tests = list(Test.objects.all())
    shuffle(tests)
    for i in range(TESTS_COUNT):
        GameResults.objects.create(game=new_game, test=tests[i])
    return new_game
