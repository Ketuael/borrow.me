from rest_framework import permissions


class IsSelf(permissions.BasePermission):
    """
    Mostly for User-based views:
        returns True, if interacts with self
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsFriend(permissions.BasePermission):
    pass


class IsInFriendship(permissions.BasePermission):
    """
    For Friendship-based views:
        returns True, if user is in friendship... :)
        (is sender / receiver and friendship is confirmed
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.confirmed and (obj.sender == user or obj.receiver == user)


class HasFriendshipRequest(permissions.BasePermission):
    """
    For Friendship-based views:
        returns True, if user is recipient site of Friendship, and didn't already confirm it
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return not obj.confirmed and obj.receiver == user


