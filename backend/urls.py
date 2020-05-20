"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path, include

from friendships import views as friend_views
from users import views as user_views
from transaction import views as transaction_views
from .api import api_root, users_api_root, friends_api_root, transactions_api_root


def go_to_api(request):
    return redirect('api/')


users_root_url = 'api/users'
friends_root_url = 'api/friends'
transactions_root_url = 'api/transactions'


urlpatterns = [
    path('', go_to_api),
    path('api/', api_root, name='api-root'),
    path(users_root_url, users_api_root, name='users-api'),
    path(friends_root_url, friends_api_root, name='friends-api'),
    path(transactions_root_url, transactions_api_root, name='transcations-api'),

]

urlpatterns += [
    path(users_root_url + '/', user_views.UserListView.as_view(), name='user-list'),
    path(users_root_url + '/create', user_views.CreateUserView.as_view(), name='user-create'),
    path(users_root_url + '/<int:pk>/', user_views.UserDetailView.as_view(), name='user-details'),
    path(users_root_url + '/<int:pk>/update', user_views.UpdateUserView.as_view(), name='user-update'),
]

urlpatterns += [
    path(friends_root_url + '/', friend_views.FriendshipListView.as_view(), name='friend-list'),
    path(friends_root_url + '/add', friend_views.AddFriendView.as_view(), name='friend-add'),
    path(friends_root_url + '/<int:pk>/', friend_views.FriendshipDetailView.as_view(), name='friend-detail'),
    path(friends_root_url + '/<int:pk>/confirmation', friend_views.ConfirmFriendshipView.as_view(),
         name='friend-confirmation'),
    path(friends_root_url + '/<int:pk>/remove', friend_views.RemoveFriendView.as_view(), name='friend-remove'),
]

urlpatterns += [
    path(transactions_root_url + '/items/', transaction_views.TransactionsListView.as_view(), name='transaction-list'),
    # path(transactions_root_url + '/money/', transaction_views.MoneyListView.as_view(), name='money-list'),
    path(transactions_root_url + '/create/item', transaction_views.CreateTransactionView.as_view(), name='transaction-create'),
    #path(transactions_root_url + '/create/money', transaction_views.CreateTransactionMoneyView.as_view(), name='money-create'),
    path(transactions_root_url + '/items/<int:pk>/update', transaction_views.UpdateTransactionView.as_view(),
         name='transaction-update'),
    # path(transactions_root_url + '/<int:pk>/balance', transaction_views.BalanceView.as_view(), name='balance-list'),
]

urlpatterns += [
                   path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
