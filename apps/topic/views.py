from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Topic, Block, Test
from .serializers import TopicSerializer, TopicDetailSerializer, BlockSerializer, BlockDetailSerializer, TestSerializer, TestDetailSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )

    def initialize_request(self, request, *args, **kwargs):
        result = super(TopicViewSet, self).initialize_request(request, *args, **kwargs)
        if self.action == 'retrieve':
            self.serializer_class = TopicDetailSerializer
        else:
            self.serializer_class = TopicSerializer
        return result


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )
    search_fields = ('name', )
    filter_fields = ('topic__id', )

    def initialize_request(self, request, *args, **kwargs):
        result = super(BlockViewSet, self).initialize_request(request, *args, **kwargs)
        if self.action == 'retrieve':
            self.serializer_class = BlockDetailSerializer
        else:
            self.serializer_class = BlockSerializer
        return result


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )
    search_fields = ('name', )
    filter_fields = ('block__id', )
