from rest_framework import generics
from rest_framework import permissions
from friendships.models import Friendship
from friendships.serializers import FriendshipListSerializer, FriendshipDetailSerializer, AddFriendSerializer, ConfirmFriendshipSerializer, RemoveFriendSerializer
from friendships.permissions import IsInFriendship, HasFriendshipRequest


# Create your views here.

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


