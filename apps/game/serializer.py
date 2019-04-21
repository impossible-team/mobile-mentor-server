from rest_framework import serializers
from ..profile.serializers import ProfileBaseInfoSerializer
from .models import Game

# class GameSerializer(serializers.HyperlinkedModelSerializer):
# #     player1 = ProfileBaseInfoSerializer(required=True)
# #
# #     game_rating = serializers.SerializerMethodField(method_name='mock')
# #
# #     class Meta:
# #         model = Game
# #         fields = ('url', 'id', 'game_rating')
# #
# #     def create(self, validated_data):
# #         user_data = validated_data.pop('user')
# #         user = UserSerializer.create(UserSerializer(), validated_data=user_data)
# #         return Profile.objects.get(user=user)
# #
# #     def mock(self, obj):
# #         return 1