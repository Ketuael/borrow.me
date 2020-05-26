from django.urls import path

from . import views as user_views

users_root_url = 'api/users'

urlpatterns = [
    path(users_root_url + '/', user_views.UserListView.as_view(), name='user-list'),
    path(users_root_url + '/login', user_views.CustomAuthToken.as_view(), name='user-login'),
    path(users_root_url + '/logout', user_views.RemoveAuthToken.as_view(), name='user-logout'),
    path(users_root_url + '/create', user_views.CreateUserView.as_view(), name='user-create'),
    path(users_root_url + '/<int:pk>/', user_views.UserDetailView.as_view(), name='user-details'),
    path(users_root_url + '/<int:pk>/update', user_views.UpdateUserView.as_view(), name='user-update'),
]

