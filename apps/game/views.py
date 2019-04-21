from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from topic.models import Test
from .models import Game
from .serializers import GameSerializer, GameCreateSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GameCreateSerializer
        return GameSerializer

    @action(methods=['post'], detail=False, url_path='(?P<pk>[^/.]+)/answers')
    def answers(self, request, *args, **kwargs):
        data = request.data
        if 'answers' not in data:
            raise ParseError('Не передан обязательный параметр `answers`')
        answers = data['answers']
        tests_ids = [int(answer['test_id']) for answer in answers]
        answers = sorted([int(answer['answer_code']) for answer in answers])
        answers_true = sorted([i[0] for i in Test.objects.values_list('correct_answer_code').filter(pk__in=tests_ids)])
        return Response(answers == answers_true)
