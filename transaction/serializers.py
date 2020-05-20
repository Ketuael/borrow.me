from django.test import TestCase
from rest_framework import serializers

from transaction.models import Transaction
from users.models import User
# Create your tests here.


class TransactionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'giver', 'taker', 'name', 'description', 'pub_date', 'due_date', 'status']


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'giver', 'taker', 'name', 'description', 'pub_date', 'due_date', 'status']

