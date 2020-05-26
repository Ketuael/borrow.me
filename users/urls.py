from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import views as user_views


@api_view(['GET'])
def users_api_root(request, format=None):
    return Response({
        'User list': reverse('user-list', request=request, format=format),
        'Create user': reverse('user-create', request=request, format=format),
        'Login (POST only)': reverse('user-login', request=request, format=format),
        'Logout (DELETE only)': reverse('user-logout', request=request, format=format),
    })


urlpatterns = [
    path('', users_api_root, name='users-api'),
    path('/', user_views.UserListView.as_view(), name='user-list'),
    path('/login', user_views.CustomAuthToken.as_view(), name='user-login'),
    path('/logout', user_views.RemoveAuthToken.as_view(), name='user-logout'),
    path('/create', user_views.CreateUserView.as_view(), name='user-create'),
    path('/<int:pk>/', user_views.UserDetailView.as_view(), name='user-details'),
    path('/<int:pk>/update', user_views.UpdateUserView.as_view(), name='user-update'),
]

