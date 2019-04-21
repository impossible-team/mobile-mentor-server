import json
from rest_framework import serializers
from profile.models import Profile
from profile.serializers import ProfileBaseInfoSerializer
from .models import Game
from topic.serializers import TestDetailSerializer, TestDetailModelSerializer
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
        l = list()
        for i in obj.results.all():
            l.append(TestDetailModelSerializer(i, context=self.context).data)
        d = dict()
        d['id'] = obj.id
        d['questions'] = l
        return d

    class Meta:
        model = Game
        fields = ('user_id', )
