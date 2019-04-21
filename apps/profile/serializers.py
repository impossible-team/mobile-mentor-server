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
    game_won = serializers.SerializerMethodField()
    game_total = serializers.SerializerMethodField()
    game_rating = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'url', 'id', 'user', 'state', 'guid', 'points',
            'topic_studied', 'topic_total',
            'game_won', 'game_total', 'game_rating'
        )

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

    def get_game_won(self, obj):
        """

        :param Profile obj:
        :return:
        """
        return obj.game_won()

    def get_game_total(self, obj):
        """

        :param Profile obj:
        :return:
        """
        return obj.game_count()

    def get_game_rating(self, obj):
        """

        :param Profile obj:
        :return:
        """
        rating = (obj.game_won() / (obj.game_count() or 1)) * 100
        if rating < 50.0:
            return 1
        elif rating < 75.0:
            return 2
        elif rating <= 100.0:
            return 3
        else:
            return 3


class ProfileBaseInfoSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    game_rating = serializers.SerializerMethodField(method_name='mock')

    class Meta:
        model = Profile
        fields = ('id', 'game_rating', 'username', )

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        return Profile.objects.get(user=user)

    def get_username(self, obj):
        return obj.user.username

    def mock(self, obj):
        return 1