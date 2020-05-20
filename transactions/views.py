from rest_framework import generics
from rest_framework import permissions
from transactions.models import Transaction, MoneyTransaction
from transactions.serializers import TransactionsListSerializer, CreateTransactionSerializer, UpdateTransactionSerializer
from transactions.serializers import MoneyTransactionsListSerializer, CreateMoneyTransactionSerializer, BalanceSerializer
from transactions.permissions import IsInTransaction
# Create your views here.


class TransactionsListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsListSerializer

    def get_queryset(self):
        user = self.request.user
        giver = Transaction.objects.filter(giver=user)
        taker = Transaction.objects.filter(taker=user)
        return giver.union(taker)

    permission_classes = [permissions.IsAuthenticated]


class CreateTransactionView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = CreateTransactionSerializer

    permission_classes = [permissions.IsAuthenticated]


class UpdateTransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = UpdateTransactionSerializer

    permission_classes = [IsInTransaction]

    # item - monetary divider


class MoneyTransactionsListView(generics.ListAPIView):
    queryset = MoneyTransaction.objects.all()
    serializer_class = MoneyTransactionsListSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        giver = MoneyTransaction.objects.filter(giver=user)
        taker = MoneyTransaction.objects.filter(taker=user)
        return giver.union(taker)


class CreateMoneyTransactionView(generics.CreateAPIView):
    queryset = MoneyTransaction.objects.all()
    serializer_class = CreateMoneyTransactionSerializer

    permission_classes = [permissions.IsAuthenticated]


