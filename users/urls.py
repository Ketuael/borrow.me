from django.urls import path
from users import views


urlpatterns = [
    path('', views.users_root, name='users-api'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/create', views.CreateUserView.as_view(), name='user-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-details'),
    path('users/<int:pk>/update', views.UpdateUserView.as_view(), name='user-update'),
    path('friends/<int:pk>/', views.FriendListView.as_view(), name='friend-list'),
    path('friends/<int:pk>/add', views.AddFriendView.as_view(), name='friend-add'),
]


