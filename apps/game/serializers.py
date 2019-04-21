from rest_framework import serializers
from profile.models import Profile
from profile.serializers import ProfileBaseInfoSerializer
from .models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):

    player1 = ProfileBaseInfoSerializer(required=True)
    player2 = ProfileBaseInfoSerializer(required=True)
    winner = ProfileBaseInfoSerializer(required=True)
    loser = ProfileBaseInfoSerializer(required=True)

    class Meta:
        model = Game
        fields = ('url', 'id', 'player1', 'player2', 'winner', 'loser', 'winner_points', 'loser_points', 'start',
                  'end', 'state')


class GameCreateSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, attrs):
        return True

    def create(self, validated_data):
        id = validated_data['user_id']
        player = Profile.objects.get(pk=id)

    class Meta:
        model = Game
