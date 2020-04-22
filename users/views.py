from rest_framework import generics
from users.models import User, Friendship
from users.serializers import UserListSerializer, UserDetailSerializer, CreateUserSerializer, UpdateUserSerializer
from users.serializers import FriendshipSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from users.permissions import IsSelf

# Create your views here.


@api_view(['GET'])
def users_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'users/create': reverse('user-create', request=request, format=format),
        'friends/': reverse('friend-list', request=request, format=format),
        'friends/add': reverse('friend-add', request=request, format=format),
    })


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'first_name', 'last_name']


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


class FriendshipListView(generics.ListAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


class AddFriendView(generics.CreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


class DetailFriendView(generics.RetrieveAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


class ManageFriendView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


