from rest_framework import generics
from users.models import User, Friendship
from users.serializers import UserListSerializer, UserDetailSerializer, CreateUserSerializer, UpdateUserSerializer
from users.serializers import FriendshipListSerializer, FriendshipDetailSerializer, AddFriendSerializer, ConfirmFriendshipSerializer, RemoveFriendSerializer
from rest_framework import filters
from rest_framework import permissions
from users.permissions import IsSelf, IsFriend, IsInFriendship, HasFriendshipRequest

# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'first_name', 'last_name']


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    #permission_classes = [IsSelf | IsFriend]


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

    permission_classes = [IsSelf]


class FriendshipListView(generics.ListAPIView):
    serializer_class = FriendshipListSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all friends (both confirmed and not) of current user (requester)
        """
        user = self.request.user
        sender = Friendship.objects.filter(sender=user)
        receiver = Friendship.objects.filter(receiver=user)
        return sender.union(receiver)


class FriendshipDetailView(generics.RetrieveAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipDetailSerializer

    permission_classes = [IsInFriendship]


class AddFriendView(generics.CreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = AddFriendSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class ConfirmFriendshipView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friendship.objects.all()
    serializer_class = ConfirmFriendshipSerializer

    permission_classes = [HasFriendshipRequest]


class RemoveFriendView(generics.RetrieveDestroyAPIView):
    queryset = Friendship.objects.all()
    serializer_class = RemoveFriendSerializer

    permission_classes = [IsInFriendship]


