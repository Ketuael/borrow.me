"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""

#from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from .api import api_root, users_api_root, friends_api_root
from users import views as user_views
from friendships import views as friend_views


def go_to_api(request):
    return redirect('api/')


users_root_url = 'api/users'
friendships_root_url = 'api/friends'


urlpatterns = [
    path('', go_to_api),
    path('api/', api_root, name='api-root'),
]

urlpatterns += [
    path(users_root_url, users_api_root, name='users-api'),
    path(users_root_url + '/', user_views.UserListView.as_view(), name='user-list'),
    path(users_root_url + '/create', user_views.CreateUserView.as_view(), name='user-create'),
    path(users_root_url + '/<int:pk>/', user_views.UserDetailView.as_view(), name='user-details'),
    path(users_root_url + '/<int:pk>/update', user_views.UpdateUserView.as_view(), name='user-update'),
]

urlpatterns += [
    path(friendships_root_url, friends_api_root, name='friends-api'),
    path(friendships_root_url + '/', friend_views.FriendshipListView.as_view(), name='friend-list'),
    path(friendships_root_url + '/add', friend_views.AddFriendView.as_view(), name='friend-add'),
    path(friendships_root_url + '/<int:pk>/', friend_views.FriendshipDetailView.as_view(), name='friend-detail'),
    path(friendships_root_url + '/<int:pk>/confirmation', friend_views.ConfirmFriendshipView.as_view(), name='friend-confirmation'),
    path(friendships_root_url + '/<int:pk>/remove', friend_views.RemoveFriendView.as_view(), name='friend-remove'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

