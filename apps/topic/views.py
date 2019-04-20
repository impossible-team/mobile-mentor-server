from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import status
from rest_framework import filters
from .models import Topic, Block, Test
from .serializers import TopicSerializer, TopicDetailSerializer, BlockSerializer, BlockDetailSerializer, TestSerializer, TestDetailSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    # filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )


