from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import views as transaction_views


@api_view(['GET'])
def transactions_api_root(request, format=None):
    return Response({
        'transactions/items/': reverse('transaction-list', request=request, format=format),
        'transactions/items/create': reverse('transaction-create', request=request, format=format),
        'transactions/money': reverse('money-list', request=request, format=format),
        'transactions/money/create': reverse('money-create', request=request, format=format),
    })


urlpatterns = [
    path('', transactions_api_root, name='transcations-api'),
    path('/items/', transaction_views.TransactionsListView.as_view(), name='transaction-list'),
    path('/items/create', transaction_views.CreateTransactionView.as_view(), name='transaction-create'),
    path('/items/<int:pk>/update', transaction_views.UpdateTransactionView.as_view(), name='transaction-update'),
]


urlpatterns += [
    path('/money/', transaction_views.MoneyTransactionsListView.as_view(), name='money-list'),
    path('/money/create', transaction_views.CreateMoneyTransactionView.as_view(), name='money-create'),
]

