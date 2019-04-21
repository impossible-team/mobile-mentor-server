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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_class = TopicDetailSerializer
        kwargs['context'] = self.get_serializer_context()
        args = args + (instance, )
        serializer = serializer_class(*args, **kwargs)
        return Response(serializer.data)


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )
    search_fields = ('name', )
    filter_fields = ('topic__id', )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_class = BlockDetailSerializer
        kwargs['context'] = self.get_serializer_context()
        serializer = serializer_class(instance)
        return Response(serializer.data)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )
    search_fields = ('name', )
    filter_fields = ('block__id', )
