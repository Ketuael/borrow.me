from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics
from rest_framework import permissions
from transaction.models import Transaction
from transaction.serializers import TransactionsListSerializer, CreateTransactionSerializer


class TransactionsListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsListSerializer


class CreateTransactionView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = CreateTransactionSerializer


