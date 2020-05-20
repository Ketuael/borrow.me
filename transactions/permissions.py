from rest_framework import permissions


class IsInTransaction(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.giver == user or obj.taker == user:
            return True
        else:
            return False

