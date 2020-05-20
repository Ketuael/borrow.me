from rest_framework import generics
from rest_framework import permissions
from transaction.models import Transaction
from transaction.serializers import TransactionsListSerializer, CreateTransactionSerializer

# Create your views here.


class TransactionsListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsListSerializer


class CreateTransactionView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = CreateTransactionSerializer


