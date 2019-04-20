from rest_framework import serializers
from .models import Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'state', 'guid')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        return Profile.objects.get(user=user)
