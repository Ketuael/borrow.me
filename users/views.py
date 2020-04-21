from rest_framework import generics
from users.models import User, Friend
from users.serializers import UserListSerializer, UserDetailSerializer, CreateUserSerializer, UpdateUserSerializer
from users.serializers import FriendSerializer, AddFriendSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from users.permissions import IsSelf

# Create your views here.


@api_view(['GET'])
def users_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'users/create': reverse('user-create', request=request, format=format),
    })


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

    permission_classes = [IsSelf]


class FriendListView(generics.RetrieveAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class AddFriendView(generics.UpdateAPIView):
    queryset = Friend.objects.all()
    serializer_class = AddFriendSerializer