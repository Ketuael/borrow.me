from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Users API': reverse('users-api', request=request, format=format),
        'Friends API': reverse('friends-api', request=request, format=format),
        'Transcations API': reverse('transcations-api', request=request, format=format),
    })

@api_view(['GET'])
def users_api_root(request, format=None):
    return Response({
        'User list': reverse('user-list', request=request, format=format),
        'Create user': reverse('user-create', request=request, format=format),
        'Login (POST only)': reverse('user-login', request=request, format=format),
        'Logout (DELETE only)': reverse('user-logout', request=request, format=format),
    })


@api_view(['GET'])
def friends_api_root(request, format=None):
    return Response({
        'Friends list': reverse('friend-list', request=request, format=format),
        'Add friend view': reverse('friend-add', request=request, format=format),
    })

@api_view(['GET'])
def transactions_api_root(request, format=None):
    return Response({
        'transactions/items/': reverse('transaction-list', request=request, format=format),
        'transactions/items/create': reverse('transaction-create', request=request, format=format),
        'transactions/money': reverse('money-list', request=request, format=format),
        'transactions/money/create': reverse('money-create', request=request, format=format),
        #'transactions/money/balance': reverse('balance', request=request, format=format),
    })


