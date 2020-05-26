from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import views as friend_views


@api_view(['GET'])
def friends_api_root(request, format=None):
    return Response({
        'Friends list': reverse('friend-list', request=request, format=format),
        'Add friend view': reverse('friend-add', request=request, format=format),
    })


urlpatterns = [
    path('', friends_api_root, name='friends-api'),
    path('/', friend_views.FriendshipListView.as_view(), name='friend-list'),
    path('/add', friend_views.AddFriendView.as_view(), name='friend-add'),
    path('/<int:pk>/', friend_views.FriendshipDetailView.as_view(), name='friend-detail'),
    path('/<int:pk>/confirmation', friend_views.ConfirmFriendshipView.as_view(), name='friend-confirmation'),
    path('/<int:pk>/remove', friend_views.RemoveFriendView.as_view(), name='friend-remove'),
]

