from rest_framework import serializers
from .models import Topic, Block, Test


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'name', )


class TestDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'name', 'content', )


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = ('id', 'name', 'short_content')


class BlockDetailSerializer(serializers.ModelSerializer):

    tests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Block
        fields = ('id', 'name', 'content', 'tests')


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'name')


class TopicDetailSerializer(serializers.ModelSerializer):

    blocks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Block
        fields = ('id', 'name', 'content', 'blocks')
