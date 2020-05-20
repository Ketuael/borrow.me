from tkinter import Entry

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from rest_framework import serializers, generics
from rest_framework.exceptions import ValidationError

from transaction.models import Transaction, Money
from users.models import User
# Create your tests here.


class TransactionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'giver', 'taker', 'name', 'description', 'pub_date', 'due_date', 'status']


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction

        fields = ['id', 'giver', 'taker', 'name', 'description', 'due_date']

        def validate(self, data):
            """
            Check that start is before finish.
            """
            if data['pub_date'] > data['due_date']:
                raise serializers.ValidationError("finish must occur after start")
            return data


class UpdateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'description', 'due_date', 'status']


class RemoveTransactionSerializer(generics.RetrieveDestroyAPIView):
    class Meta:
        model = Transaction
        fields = ['id', 'giver', 'taker', 'name', 'description', 'due_date', 'status']


class ConfirmTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['giver', 'taker', 'status']
        extra_kwargs = {'sender': {'read_only': True}, 'receiver': {'read_only': True}}

        def update(self, instance, validated_data):
            instance.status = validated_data['status']
            instance.save()
            return instance


class TransactionsMoneyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = ['id', 'giver', 'taker', 'ammount']


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = ['id', 'giver', 'taker', 'ammount']

        def create(self, validated_data, balance=0):
            value = validated_data['ammount']
            sender = validated_data['giver']
            receiver = validated_data['taker']
            a = validated_data['giver']
            b = validated_data['taker']
            for e in Entry.objects.all(giver = sender):
                if validated_data['giver'] == sender:
                    balance -= value
                else:
                    if validated_data['taker'] == b:
                        balance += value
                return balance


class CreateTransactionMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = ['id', 'giver', 'taker', 'ammount']
