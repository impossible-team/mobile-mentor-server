from rest_framework import serializers
from profile.models import Profile
from profile.serializers import ProfileBaseInfoSerializer
from .models import Game
from game_brain import api as brain

class GameSerializer(serializers.ModelSerializer):

    player1 = ProfileBaseInfoSerializer()
    player2 = ProfileBaseInfoSerializer()
    winner = ProfileBaseInfoSerializer()
    loser = ProfileBaseInfoSerializer()

    class Meta:
        model = Game
        fields = ('url', 'id', 'player1', 'player2', 'winner', 'loser', 'winner_points', 'loser_points', 'start_time',
                  'end_time', 'state')


class GameCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        id = validated_data['user_id']
        player = Profile.objects.get(pk=id)
        return brain.get_game(player)

    def to_representation(self, obj):
        return GameSerializer(obj, context=self.context).data

    class Meta:
        model = Game
        fields = ('user_id', )
