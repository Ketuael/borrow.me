from django.urls import path
from users import views


urlpatterns = [
    path('', views.api_root),
    path('users', views.users_root, name='users-api'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/create', views.CreateUserView.as_view(), name='user-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-details'),
    path('users/<int:pk>/update', views.UpdateUserView.as_view(), name='user-update'),
]

urlpatterns += [
    path('friends', views.friends_root, name='friends-api'),
    path('friends/', views.FriendshipListView.as_view(), name='friend-list'),
    path('friends/add', views.AddFriendView.as_view(), name='friend-add'),
    path('friends/<int:pk>', views.DetailFriendView.as_view(), name='friend-detail'),
    path('friends/<int:pk>/manage', views.ManageFriendView.as_view(), name='friend-manage'),
]


