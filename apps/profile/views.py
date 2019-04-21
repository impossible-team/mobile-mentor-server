from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import status
from .models import Profile, User
from .serializers import ProfileSerializer, UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-user__username')
    serializer_class = ProfileSerializer


class LoginAPIView(APIView):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        if 'username' not in data:
            raise exceptions.ParseError(detail='Поле `username` отсутствует')

        user, created = User.objects.get_or_create(username=data['username'])
        profile = Profile.objects.get(user=user)
        profile_serializer = ProfileSerializer(profile, context={'request': request})
        return Response(profile_serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
