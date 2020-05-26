from django.urls import path

from . import views as transaction_views

transactions_root_url = 'api/transactions'

urlpatterns = [
    path(transactions_root_url + '/items/', transaction_views.TransactionsListView.as_view(), name='transaction-list'),
    path(transactions_root_url + '/items/create', transaction_views.CreateTransactionView.as_view(), name='transaction-create'),
    path(transactions_root_url + '/items/<int:pk>/update', transaction_views.UpdateTransactionView.as_view(), name='transaction-update'),
]


urlpatterns += [
    path(transactions_root_url + '/money/', transaction_views.MoneyTransactionsListView.as_view(), name='money-list'),
    path(transactions_root_url + '/money/create', transaction_views.CreateMoneyTransactionView.as_view(), name='money-create'),
]

