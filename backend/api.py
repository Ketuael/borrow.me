from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Users API': reverse('users-api', request=request, format=format),
        'Friends API': reverse('friends-api', request=request, format=format),
    })

@api_view(['GET'])
def users_api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'users/create': reverse('user-create', request=request, format=format),
    })


@api_view(['GET'])
def friends_api_root(request, format=None):
    return Response({
        'friends/': reverse('friend-list', request=request, format=format),
        'friends/add': reverse('friend-add', request=request, format=format),
    })