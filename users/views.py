from rest_framework import generics
from users.models import User, Friendship
from users.serializers import UserListSerializer, UserDetailSerializer, CreateUserSerializer, UpdateUserSerializer
from users.serializers import FriendshipListSerializer, FriendshipDetailSerializer, AddFriendSerializer, ConfirmFriendshipSerializer, RemoveFriendSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from users.permissions import IsSelf

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Users API': reverse('users-api', request=request, format=format),
        'Friends API': reverse('friends-api', request=request, format=format),
    })

@api_view(['GET'])
def users_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'users/create': reverse('user-create', request=request, format=format),
    })


@api_view(['GET'])
def friends_root(request, format=None):
    return Response({
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
    serializer_class = FriendshipListSerializer


class FriendshipDetailView(generics.RetrieveAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipDetailSerializer


class AddFriendView(generics.CreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = AddFriendSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class ConfirmFriendshipView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friendship.objects.all()
    serializer_class = ConfirmFriendshipSerializer


class RemoveFriendView(generics.RetrieveDestroyAPIView):
    queryset = Friendship.objects.all()
    serializer_class = RemoveFriendSerializer


