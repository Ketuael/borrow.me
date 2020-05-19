from rest_framework import permissions
from friendships.models import Friendship
from users.models import User


class IsSelf(permissions.BasePermission):
    """
    For User-based views:
        returns True if interacts with self
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsFriend(permissions.BasePermission):
    """
    For User-based views:
        returns True if is friend of spoken user
    """
    def has_object_permission(self, request, view, obj):
        if not isinstance(request.user, User):
            return False

        friends1 = Friendship.objects.filter(sender=request.user)
        friends2 = Friendship.objects.filter(receiver=request.user)
        friends = friends1.union(friends2)

        for friend in friends:
            if friend.sender == obj and friend.confirmed:
                return True
            elif friend.receiver == obj and friend.confirmed:
                return True

        return False
