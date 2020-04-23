from rest_framework import permissions


class IsSelf(permissions.BasePermission):
<<<<<<< HEAD
=======
    """
    Mostly for User-based views:
        returns True, if interacts with self
    """
>>>>>>> develop

    def has_object_permission(self, request, view, obj):
        return obj == request.user


<<<<<<< HEAD
=======
class IsFriend(permissions.BasePermission):
    pass
>>>>>>> develop

