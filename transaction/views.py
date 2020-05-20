from rest_framework import generics
from rest_framework import permissions
from transaction.models import Transaction
from transaction.serializers import TransactionsListSerializer, CreateTransactionSerializer, UpdateTransactionSerializer, RemoveTransactionSerializer, ConfirmTransactionSerializer
from transaction.permissions import HasTransactionRequest
# Create your views here.


class TransactionsListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsListSerializer


class CreateTransactionView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = CreateTransactionSerializer


class UpdateTransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = UpdateTransactionSerializer


class RemoveTransactionView(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = RemoveTransactionSerializer


class ConfirmTransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = ConfirmTransactionSerializer

    permission_classes = [HasTransactionRequest]

