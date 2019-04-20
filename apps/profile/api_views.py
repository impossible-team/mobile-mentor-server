from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-user__username')
    serializer_class = ProfileSerializer


class LoginAPIView(CreateAPIView):

    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # type: UserSerializer
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        profile = Profile.objects.get(user=serializer.data['id'])
        profile_serializer = ProfileSerializer(profile)
        return Response(profile_serializer.data, status=HTTP_201_CREATED, headers=headers)
