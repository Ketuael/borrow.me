from django.test import TestCase
from rest_framework import serializers

from transaction.models import Transaction
from users.models import User
# Create your tests here.


class TransactionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['sender', 'receiver', 'nazwa', 'opis', 'pub_date', 'due_date', 'status', 'photo']


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['sender', 'receiver', 'nazwa', 'opis', 'pub_date', 'due_date', 'status', 'photo']

    def create(self, validated_data):
        transaction = Transaction.objects.create_user(**validated_data)
        transaction.save()
        return transaction
