from rest_framework import permissions


class HasTransactionRequest(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        return not obj.confirmed and obj.receiver == user


