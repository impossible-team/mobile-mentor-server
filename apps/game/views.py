from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer, GameCreateSerializer
from game_brain import api as brain_api


class GameViewSet(viewsets.ViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GameCreateSerializer
        return GameSerializer