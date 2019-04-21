from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from profile.models import Profile
from .models import Topic, Block, Test
from .serializers import TopicSerializer, TopicDetailSerializer, BlockSerializer, BlockDetailSerializer, TestSerializer, TestDetailSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TopicDetailSerializer
        else:
            return TopicSerializer

    @action(methods=['get'], detail=False, url_path='(?P<pk>[^/.]+)/generate_tests')
    def generate_tests(self, request, *args, **kwargs):
        params = request.query_params
        if 'count' not in params:
            count = 1
        else:
            try:
                count = int(params['count'])
            except ValueError:
                raise ParseError('Неверный тип переданного значения `count`: {}'.format(type(params['count'])))
        topic = self.get_object()  # type: Topic
        tests_qs = topic.get_random_tests(count)
        serializer = TestDetailSerializer(tests_qs, many=True)
        return Response(serializer.data)


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )
    search_fields = ('name', )
    filter_fields = ('topic__id', )

    def get_serializer_class(self):
        if self.action in ['retrieve', 'studied']:
            return BlockDetailSerializer
        else:
            return BlockSerializer

    @action(methods=['post'], detail=False, url_path='(?P<pk>[^/.]+)/studies')
    def studied(self, request,  *args, **kwargs):
        data = request.data
        if 'user_id' not in data:
            raise ParseError('Не передано обязательное значение `user_id`')
        user_id = data['user_id']
        try:
            profile = Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            raise NotFound()
        instance = self.get_object()
        profile.blocks.add(instance)
        serializer=self.get_serializer(instance)
        return Response(serializer.data)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )
    search_fields = ('name', )
    filter_fields = ('block__id', )
