from rest_framework import generics
from rest_framework import permissions
from transaction.models import Transaction, Money
from transaction.serializers import TransactionsListSerializer, CreateTransactionSerializer, UpdateTransactionSerializer, RemoveTransactionSerializer, ConfirmTransactionSerializer, TransactionsMoneyListSerializer, BalanceSerializer, CreateTransactionMoneySerializer
from transaction.permissions import IsInTransaction
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


class UpdateTransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = UpdateTransactionSerializer
    permission_classes = [IsInTransaction]


class RemoveTransactionView(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = RemoveTransactionSerializer


class MoneyListView(generics.ListAPIView):
    queryset = Money.objects.all()
    serializer_class = TransactionsMoneyListSerializer


class BalanceView(generics.ListAPIView):
    queryset = Money.objects.all()
    serializer_class = BalanceSerializer


class CreateTransactionMoneyView(generics.CreateAPIView):
    queryset = Money.objects.all()
    serializer_class = CreateTransactionMoneySerializer

