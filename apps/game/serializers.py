from rest_framework import serializers
from profile.models import Profile
from profile.serializers import ProfileBaseInfoSerializer
from .models import Game
from game_brain import api as brain

class GameSerializer(serializers.HyperlinkedModelSerializer):

    player1 = ProfileBaseInfoSerializer()
    player2 = ProfileBaseInfoSerializer()
    winner = ProfileBaseInfoSerializer()
    loser = ProfileBaseInfoSerializer()

    class Meta:
        model = Game
        fields = ('url', 'id', 'player1', 'player2', 'winner', 'loser', 'winner_points', 'loser_points', 'start',
                  'end', 'state')


class GameCreateSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.IntegerField()

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        id = validated_data['user_id']
        player = Profile.objects.get(pk=id)
        return brain.get_game(player)

    class Meta:
        model = Game
        fields = ('user_id',)
