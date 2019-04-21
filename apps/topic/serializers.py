from rest_framework import serializers
from .models import Topic, Block, Test


class TestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'name', )


class TestDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'name', 'content', )


class BlockSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Block
        fields = ('id', 'name', )


class BlockDetailSerializer(serializers.HyperlinkedModelSerializer):

    tests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Block
        fields = ('id', 'name', 'content', 'tests')


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'name', 'url', )


class TopicDetailSerializer(serializers.HyperlinkedModelSerializer):

    blocks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'url', 'blocks')
