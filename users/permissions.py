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

