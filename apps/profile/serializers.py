from rest_framework import serializers
from topic.models import Topic
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


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)

    topic_studied = serializers.SerializerMethodField()
    topic_total = serializers.SerializerMethodField()
    game_won = serializers.SerializerMethodField(method_name='mock')
    game_total = serializers.SerializerMethodField(method_name='mock')
    game_rating = serializers.SerializerMethodField(method_name='mock')

    class Meta:
        model = Profile
        fields = ('url', 'id', 'user', 'state', 'guid', 'points', 'topic_studied', 'topic_total', 'game_won', 'game_total', 'game_rating')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        return Profile.objects.get(user=user)

    def get_topic_studied(self, obj):
        """
        Количество изученных тем
        :param Profile obj:
        :return:
        """
        return obj.topic_studied_count()

    def get_topic_total(self, obj):
        """
        Общее количетсво тем

        :param Profile obj:
        :return:
        """
        return Topic.objects.count()

    def mock(self, obj):
        return 1


class ProfileBaseInfoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)

    game_rating = serializers.SerializerMethodField(method_name='mock')

    class Meta:
        model = Profile
        fields = ('url', 'id', 'user', 'game_rating')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        return Profile.objects.get(user=user)

    def mock(self, obj):
        return 1