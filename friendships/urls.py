from django.urls import path

from . import views as friend_views

friends_root_url = 'api/friends'

urlpatterns = [
    path(friends_root_url + '/', friend_views.FriendshipListView.as_view(), name='friend-list'),
    path(friends_root_url + '/add', friend_views.AddFriendView.as_view(), name='friend-add'),
    path(friends_root_url + '/<int:pk>/', friend_views.FriendshipDetailView.as_view(), name='friend-detail'),
    path(friends_root_url + '/<int:pk>/confirmation', friend_views.ConfirmFriendshipView.as_view(), name='friend-confirmation'),
    path(friends_root_url + '/<int:pk>/remove', friend_views.RemoveFriendView.as_view(), name='friend-remove'),
]

