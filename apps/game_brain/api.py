from profile.models import Profile
from game.models import Game

def start_game(player=Profile):
    waiter_players = Profile.objects.order_by('?').filter(state__exact=Profile.STATE_READY_TO_PLAY)
    return None

