from rest_framework import generics
from rest_framework import permissions
from transaction.models import Transaction
from transaction.serializers import TransactionsListSerializer, CreateTransactionSerializer, UpdateTransactionSerializer
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

    permission_classes = [permissions.IsAuthenticated]


class UpdateTransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = UpdateTransactionSerializer

    permission_classes = [IsInTransaction]

