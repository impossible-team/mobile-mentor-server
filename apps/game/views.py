from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from topic.models import Test
from .models import Game, GameResults
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
        game = self.get_object()
        data = request.data
        if 'user_id' not in data:
            raise ParseError('Не передан обязательный параметр `answers`')
        user_id = data['user_id']
        if 'answers' not in data:
            raise ParseError('Не передан обязательный параметр `answers`')
        answers = data['answers']
        tests_ids = [int(answer['test_id']) for answer in answers]
        answers = {answer['test_id']: answer['answer_code'] for answer in answers}
        answers_true = {t['id']: t['correct_answer_code'] for t in
                        Test.objects.values('id', 'correct_answer_code').filter(pk__in=list(answers.keys()))}
        for test_id in tests_ids:
            game_result = GameResults.objects.filter(game=game, test__pk=test_id).get()
            if game.player1.pk == user_id:
                game_result.player1=answers_true[test_id] == answers[test_id]
            elif game.player1.pk == user_id:
                game_result.update(player1=answers_true[test_id] == answers[test_id])
            game_result.save()
        return Response(status=HTTP_200_OK)
