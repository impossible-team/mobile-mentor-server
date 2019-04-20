from rest_framework import serializers
from .models import Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

    def validate_username(self, value):
        value = str(value).strip()
        if not value:
            raise serializers.ValidationError('Имя пользователя не может быть пустым')
        return value


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    topic_studied = serializers.SerializerMethodField(method_name='mock')
    topic_total = serializers.SerializerMethodField(method_name='mock')
    game_won = serializers.SerializerMethodField(method_name='mock')
    game_total = serializers.SerializerMethodField(method_name='mock')
    game_rating = serializers.SerializerMethodField(method_name='mock')

    class Meta:
        model = Profile
        fields = ('id', 'user', 'state', 'guid', 'points', 'topic_studied', 'topic_total', 'game_won', 'game_total', 'game_rating')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        return Profile.objects.get(user=user)

    def mock(self, obj):
        return 1
